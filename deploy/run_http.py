"""Run the Buildium MCP server over HTTP so other containers can reach it.

The project's own entry point (`main()`) uses stdio. This wrapper serves the same server on a network
port. The server has no login of its own: always run it behind the gate in docker-compose.prod.yml.
"""

import os

from mcp_server_buildium.server import create_server

create_server().run(transport="http", host="0.0.0.0", port=int(os.environ.get("MCP_PORT", "8000")))
