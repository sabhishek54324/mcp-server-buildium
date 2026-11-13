FROM python:3.12-slim
WORKDIR /app
COPY . /app/mcp-server-buildium
RUN pip install --no-cache-dir /app/mcp-server-buildium \
 && useradd --create-home --uid 10001 mcp
COPY deploy/run_http.py /app/run_http.py
USER mcp
ENV MCP_PORT=8000
# Safe default: the Buildium sandbox. An env file or compose setting overrides it. (Without this the server
# defaults to PRODUCTION.)
ENV BUILDIUM_BASE_URL=https://apisandbox.buildium.com
CMD ["python", "/app/run_http.py"]
