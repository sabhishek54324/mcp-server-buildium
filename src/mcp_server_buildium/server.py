"""Main MCP server entry point for Buildium."""

from collections.abc import Callable
from typing import Any

from fastmcp import FastMCP

from .buildium_client import BuildiumClient
from .config import BuildiumConfig
from .tools.applicants import register_applicant_tools
from .tools.associations import register_association_tools
from .tools.bank_accounts import register_bank_account_tools
from .tools.bills import register_bill_tools
from .tools.files import register_file_tools
from .tools.leases import register_lease_tools
from .tools.owners import register_owner_tools
from .tools.rentals import register_rental_tools
from .tools.tasks import register_task_tools
from .tools.tenants import register_tenant_tools
from .tools.units import register_unit_tools
from .tools.generated import register_generated_tools
from .tools.vendors import register_vendor_tools

# Tool category (the BUILDIUM_CATEGORIES name) -> the function that registers it.
CATEGORIES: dict[str, Callable[[FastMCP, BuildiumClient], None]] = {
    "associations": register_association_tools,
    "leases": register_lease_tools,
    "rentals": register_rental_tools,
    "applicants": register_applicant_tools,
    "tenants": register_tenant_tools,
    "owners": register_owner_tools,
    "units": register_unit_tools,
    "vendors": register_vendor_tools,
    "tasks": register_task_tools,
    "bills": register_bill_tools,
    "files": register_file_tools,
    "bank_accounts": register_bank_account_tools,
    # Every other Buildium API operation (generated from the published spec, 2026-11-19).
    "all_endpoints": register_generated_tools,
}


def create_server(
    config: BuildiumConfig | None = None, client: BuildiumClient | None = None
) -> FastMCP:
    """Build the MCP server with the tools of every enabled category.

    Args:
        config: Buildium configuration. If None, loads from environment.
        client: Buildium client. If None, one is built from ``config``.

    Returns:
        The configured FastMCP server.
    """
    config = config or (client.config if client else BuildiumConfig.from_env())
    unknown = (config.get_enabled_categories() or set()) - CATEGORIES.keys()
    if unknown:
        raise ValueError(
            f"BUILDIUM_CATEGORIES has unknown categories {sorted(unknown)}; "
            f"known categories are {sorted(CATEGORIES)}"
        )
    client = client or BuildiumClient(config=config)
    mcp = FastMCP("buildium")
    target = _FilteredMCP(mcp, config)
    for category, register in CATEGORIES.items():
        if config.is_category_enabled(category):
            register(target, client)  # type: ignore[arg-type]
    return mcp


class _FilteredMCP:
    """Passes tool registrations through to FastMCP, skipping the ones the config leaves out.

    BUILDIUM_TOOL_ACCESS=read keeps only get_* and list_* tools. BUILDIUM_TOOL_TAGS keeps only the
    generated tools whose Buildium area (the "[Tag]" at the start of their description) is listed.
    """

    def __init__(self, mcp: FastMCP, config: BuildiumConfig) -> None:
        self._mcp = mcp
        self._read_only = config.tool_access == "read"
        self._tags = config.allowed_tags()

    def _allowed(self, name: str, description: str | None) -> bool:
        if self._read_only and not name.startswith(("get_", "list_")):
            return False
        if self._tags is not None and description and description.startswith("["):
            tag = description[1 : description.index("]")].strip().lower()
            if tag not in self._tags:
                return False
        return True

    def tool(self, *args: Any, **kwargs: Any) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
        def decorator(fn: Callable[..., Any]) -> Callable[..., Any]:
            name = kwargs.get("name") or fn.__name__
            if not self._allowed(name, kwargs.get("description")):
                return fn
            return self._mcp.tool(*args, **kwargs)(fn)  # type: ignore[no-any-return]

        return decorator

    def __getattr__(self, attr: str) -> Any:
        return getattr(self._mcp, attr)


def main() -> None:
    """Run the MCP server (stdio by default)."""
    create_server().run()


if __name__ == "__main__":
    main()
