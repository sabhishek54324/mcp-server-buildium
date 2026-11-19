"""Generated tools: full coverage of the Buildium spec, safe names, and the HTTP call shape."""

import asyncio
import json
import re
from pathlib import Path

import httpx
import pytest

from mcp_server_buildium.tools.generated import GENERATED_TOOL_COUNT

ROOT = Path(__file__).resolve().parent.parent
SPEC = json.loads((ROOT / "specs/buildium-openapi-2026-11-19.json").read_text(encoding="utf-8"))
MANIFEST = json.loads((ROOT / "specs/generated-tools.json").read_text(encoding="utf-8"))
WRITE_PREFIXES = ("create_", "update_", "delete_", "remove_", "cancel_", "void_", "send_", "apply_", "add_")


def snake(s):
    s = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", s)
    s = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", s)
    return re.sub(r"[^A-Za-z0-9]+", "_", s).lower().strip("_")


def test_every_spec_operation_has_a_tool():
    ops = {o["operationId"] for p in SPEC["paths"].values() for m, o in p.items()
           if m in ("get", "post", "put", "patch", "delete")}
    src = "".join(p.read_text(encoding="utf-8") for p in (ROOT / "src/mcp_server_buildium/tools").glob("*.py")
                  if p.name != "generated.py")
    used = set(re.findall(r"_api\.(external_api_[a-z0-9_]+)", src))
    hand = {op for op in ops if snake(op) in used or snake(op) + "_async" in used}
    generated = {m["operationId"] for m in MANIFEST}
    assert hand.isdisjoint(generated)
    assert hand | generated == ops
    assert len(MANIFEST) == GENERATED_TOOL_COUNT


def test_generated_names_are_unique_and_safe():
    names = [m["tool"] for m in MANIFEST]
    assert len(names) == len(set(names))
    for m in MANIFEST:
        if m["method"] == "GET":
            assert m["tool"].startswith(("get_", "list_")), m
        else:
            assert m["tool"].startswith(WRITE_PREFIXES), m
            assert not m["tool"].startswith(("get_", "list_")), m


def test_server_registers_all_tools(monkeypatch):
    monkeypatch.setenv("BUILDIUM_CLIENT_ID", "id")
    monkeypatch.setenv("BUILDIUM_CLIENT_SECRET", "secret")
    from mcp_server_buildium.server import create_server

    mcp = create_server()
    tools = asyncio.run(mcp.list_tools())
    names = {t.name for t in tools}
    assert {m["tool"] for m in MANIFEST} <= names
    assert len(names) == 81 + GENERATED_TOOL_COUNT


def test_raw_request_builds_the_call(monkeypatch):
    from mcp_server_buildium.buildium_client import BuildiumClient
    from mcp_server_buildium.config import BuildiumConfig

    seen = {}

    def handler(request):
        seen["method"], seen["url"] = request.method, str(request.url)
        seen["id"] = request.headers.get("x-buildium-client-id")
        seen["body"] = request.content.decode() or None
        if request.method == "GET":
            return httpx.Response(200, json=[{"Id": 1}, {"Id": 2}])
        return httpx.Response(201, json={"Id": 9})

    real = httpx.AsyncClient
    monkeypatch.setattr(httpx, "AsyncClient", lambda **kw: real(transport=httpx.MockTransport(handler), **kw))
    client = BuildiumClient(config=BuildiumConfig(client_id="id", client_secret="secret",
                                                  base_url="https://api.buildium.com"))
    got = asyncio.run(client.raw_request("GET", "/v1/leases/{leaseId}/charges", path_params={"leaseId": 7},
                                         query={"limit": 5, "orderby": None}))
    assert got == {"items": [{"Id": 1}, {"Id": 2}], "count": 2}
    assert seen["url"] == "https://api.buildium.com/v1/leases/7/charges?limit=5" and seen["id"] == "id"
    made = asyncio.run(client.raw_request("POST", "/v1/workorders", body={"Title": "x"}))
    assert made == {"Id": 9} and json.loads(seen["body"]) == {"Title": "x"}


def test_raw_request_error_has_no_secret(monkeypatch):
    from mcp_server_buildium.buildium_client import BuildiumClient
    from mcp_server_buildium.config import BuildiumConfig

    real = httpx.AsyncClient
    monkeypatch.setattr(httpx, "AsyncClient", lambda **kw: real(
        transport=httpx.MockTransport(lambda r: httpx.Response(401, text="Unauthorized")), **kw))
    client = BuildiumClient(config=BuildiumConfig(client_id="id", client_secret="topsecret",
                                                  base_url="https://api.buildium.com"))
    with pytest.raises(ValueError) as err:
        asyncio.run(client.raw_request("GET", "/v1/workorders"))
    assert "401" in str(err.value) and "topsecret" not in str(err.value)


def test_read_only_and_tag_filters(monkeypatch):
    monkeypatch.setenv("BUILDIUM_CLIENT_ID", "id")
    monkeypatch.setenv("BUILDIUM_CLIENT_SECRET", "secret")
    monkeypatch.setenv("BUILDIUM_TOOL_ACCESS", "read")
    monkeypatch.setenv("BUILDIUM_TOOL_TAGS", "Leases,Lease Transactions,Work Orders")
    from mcp_server_buildium.server import create_server

    names = {t.name for t in asyncio.run(create_server().list_tools())}
    assert names and all(n.startswith(("get_", "list_")) for n in names)
    assert "get_lease_outstanding_balances" in names and "get_all_work_orders" in names
    assert "create_work_order" not in names and "list_leases" in names  # hand-written reads stay
    assert "get_all_announcements" not in names  # another area
