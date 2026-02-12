"""
SimpleMem MCP Server - Main Entry Point

Run this module to start the standalone MCP server.
"""


def main():
    """Main entry point for the simplemem-mcp command"""
    import uvicorn
    from .http_server import app

    # Get host and port from environment or use defaults
    import os

    host = os.getenv("MCP_HOST", "0.0.0.0")
    port = int(os.getenv("MCP_PORT", "8000"))

    print(f"Starting SimpleMem MCP Server on {host}:{port}")
    uvicorn.run(app, host=host, port=port)


if __name__ == "__main__":
    main()
