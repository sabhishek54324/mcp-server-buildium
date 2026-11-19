#!/usr/bin/env python3
"""Generate one MCP tool for every Buildium API operation the hand-written tools do not cover.

Source: specs/buildium-openapi-2026-11-19.json (Buildium's Open API v1 as published on
developer.buildium.com, saved 2026-11-19). Output: src/mcp_server_buildium/tools/generated.py.

Naming rule (safety): a tool's name starts with its action, decided by the HTTP method.
  GET                -> get_* or list_*
  POST               -> create_* (or another write verb the operation already uses)
  PUT / PATCH        -> update_*
  DELETE             -> delete_*
Agents that must not write deny the write prefixes (create_*, update_*, delete_*, ...) at the proxy,
so every generated write tool is covered by those rules automatically.

Run:  python3 scripts/gen_all_tools.py   (then run the tests)
"""

import json
import keyword
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SPEC = ROOT / "specs" / "buildium-openapi-2026-11-19.json"
OUT = ROOT / "src" / "mcp_server_buildium" / "tools" / "generated.py"
MANIFEST = ROOT / "specs" / "generated-tools.json"

WRITE_PREFIXES = ("create_", "update_", "delete_", "remove_", "cancel_", "void_", "send_", "apply_", "add_")
METHOD_PREFIX = {"post": "create_", "put": "update_", "patch": "update_", "delete": "delete_"}
TYPES = {"integer": "int", "number": "float", "boolean": "bool", "string": "str"}


def snake(s: str) -> str:
    s = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", s)
    s = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", s)
    s = re.sub(r"[^A-Za-z0-9]+", "_", s)
    return s.lower().strip("_")


def used_sdk_methods() -> set[str]:
    out = subprocess.run(["grep", "-rhoE", r"_api\.external_api_[a-z0-9_]+", str(ROOT / "src/mcp_server_buildium/tools")],
                         capture_output=True, text=True).stdout.split()
    return {re.sub(r"^_api\.", "", u) for u in out}


def existing_tool_names() -> set[str]:
    out = subprocess.run(["grep", "-rhoE", r"async def [a-z0-9_]+\(",
                          *[str(p) for p in (ROOT / "src/mcp_server_buildium/tools").glob("*.py") if p.name != "generated.py"]],
                         capture_output=True, text=True).stdout.split("\n")
    return {re.sub(r"async def ([a-z0-9_]+)\(", r"\1", o.strip()) for o in out if o.strip()}


def resolve(spec: dict, obj: dict) -> dict:
    while isinstance(obj, dict) and "$ref" in obj:
        node = spec
        for part in obj["$ref"].lstrip("#/").split("/"):
            node = node[part]
        obj = node
    return obj


def py_type(spec: dict, schema: dict) -> str:
    schema = resolve(spec, schema or {})
    t = schema.get("type")
    if t == "array":
        return f"list[{py_type(spec, schema.get('items', {}))}]"
    return TYPES.get(t, "str")


def clean(text: str, limit: int = 900) -> str:
    text = re.sub(r"<[^>]+>", " ", text or "")
    text = re.sub(r"\s+", " ", text).strip()
    return (text[: limit - 3] + "...") if len(text) > limit else text


def ident(name: str, taken: set[str]) -> str:
    base = snake(name) or "param"
    if keyword.iskeyword(base) or base in ("body", "client", "mcp"):
        base += "_"
    out, n = base, 2
    while out in taken:
        out, n = f"{base}_{n}", n + 1
    taken.add(out)
    return out


def tool_name(method: str, op_id: str, tag: str, taken: set[str]) -> str:
    action = op_id.split("_", 1)[-1]
    name = snake(action)
    if method == "get":
        if not name.startswith(("get_", "list_")):
            name = "get_" + name
    elif not name.startswith(WRITE_PREFIXES):
        name = METHOD_PREFIX[method] + name
    if name in taken:
        name = f"{name}_{snake(tag)}"
    n = 2
    while name in taken:
        name, n = f"{name}_{n}", n + 1
    taken.add(name)
    return name


def main() -> None:
    spec = json.loads(SPEC.read_text(encoding="utf-8"))
    covered = used_sdk_methods()
    taken = set(existing_tool_names())
    tools, manifest = [], []
    for path, item in spec["paths"].items():
        shared = item.get("parameters", [])
        for method in ("get", "post", "put", "patch", "delete"):
            op = item.get(method)
            if not op:
                continue
            op_id = op["operationId"]
            if snake(op_id) in covered or snake(op_id) + "_async" in covered:
                continue
            tag = (op.get("tags") or ["buildium"])[0]
            name = tool_name(method, op_id, tag, taken)
            params, names = [], set()
            for p in shared + op.get("parameters", []):
                p = resolve(spec, p)
                if p.get("in") not in ("path", "query"):
                    continue
                params.append({
                    "api": p["name"], "py": ident(p["name"], names), "in": p["in"],
                    "type": py_type(spec, p.get("schema") or p),
                    "required": bool(p.get("required")) or p["in"] == "path",
                    "doc": clean(p.get("description", ""), 300),
                })
            body = op.get("requestBody")
            body_kind = None
            if body:
                body = resolve(spec, body)
                content = body.get("content", {})
                body_kind = "json" if "application/json" in content else ("multipart" if "multipart/form-data" in content else "json")
            doc = clean(f"{op.get('summary', '')}. {op.get('description', '')}")
            manifest.append({"tool": name, "method": method.upper(), "path": path, "operationId": op_id, "tag": tag})
            tools.append((name, method.upper(), path, params, body_kind, bool(body and body.get("required")), doc, tag))

    lines = [
        '"""Generated Buildium tools: one per Buildium API operation not covered by the hand-written tools.',
        "",
        "DO NOT EDIT BY HAND. Regenerate with scripts/gen_all_tools.py from specs/buildium-openapi-2026-11-19.json.",
        "Write tools are named create_*, update_* or delete_* by HTTP method, so agents can deny them by prefix.",
        '"""',
        "",
        "from typing import Annotated, Any",
        "",
        "from fastmcp import FastMCP",
        "from pydantic import Field",
        "",
        "from ..buildium_client import BuildiumClient",
        "",
        f"GENERATED_TOOL_COUNT = {len(tools)}",
        "",
        "",
        "def register_generated_tools(mcp: FastMCP, client: BuildiumClient) -> None:",
        '    """Register every generated Buildium tool."""',
        "",
    ]
    for name, method, path, params, body_kind, body_required, doc, tag in tools:
        sig = []
        ordered = [p for p in params if p["required"]] + [p for p in params if not p["required"]]
        if body_kind and body_required:
            sig.append('        body: Annotated[dict[str, Any], Field(description="Request body as Buildium documents it (JSON object).")],')
        for p in ordered:
            ann = f'Annotated[{p["type"]}, Field(description={json.dumps(p["doc"] or p["api"])})]'
            if p["required"]:
                sig.append(f'        {p["py"]}: {ann},')
            else:
                sig.append(f'        {p["py"]}: Annotated[{p["type"]} | None, Field(description={json.dumps(p["doc"] or p["api"])})] = None,')
        if body_kind and not body_required:
            sig.append('        body: Annotated[dict[str, Any] | None, Field(description="Request body as Buildium documents it (JSON object).")] = None,')
        pathmap = "{" + ", ".join(f'{json.dumps(p["api"])}: {p["py"]}' for p in params if p["in"] == "path") + "}"
        querymap = "{" + ", ".join(f'{json.dumps(p["api"])}: {p["py"]}' for p in params if p["in"] == "query") + "}"
        desc = f"[{tag}] {doc}" + (" (multipart upload in Buildium; send fields as a JSON object)" if body_kind == "multipart" else "")
        lines += [
            f"    @mcp.tool(name={json.dumps(name)}, description={json.dumps(desc)})",
            f"    async def {name}(",
            *sig,
            "    ) -> dict[str, Any]:",
            f"        return await client.raw_request({json.dumps(method)}, {json.dumps(path)}, path_params={pathmap}, "
            f"query={querymap}, body={'body' if body_kind else 'None'})",
            "",
        ]
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n") if hasattr(OUT, "write_text") else None
    MANIFEST.write_text(json.dumps(manifest, indent=1) + "\n", encoding="utf-8")
    print(f"generated {len(tools)} tools -> {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
