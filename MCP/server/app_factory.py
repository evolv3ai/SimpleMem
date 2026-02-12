"""
FastAPI App Factory for SimpleMem MCP Server

This module provides a factory function to create a FastAPI app instance
that can be used standalone or mounted in another FastAPI application.

Usage:
    # Standalone
    from simplemem_mcp import create_app
    app = create_app()

    # Mount in another app with prefix
    from simplemem_mcp import create_app
    main_app = FastAPI()
    mcp_app = create_app(include_cors=False, include_static=False)
    main_app.mount("/simplemem", mcp_app)
"""

from fastapi import FastAPI

# Import the app from http_server
from .http_server import app as _default_app


def create_app(
    include_cors: bool = True,
    include_static: bool = True,
) -> FastAPI:
    """
    Get the configured FastAPI app instance for SimpleMem MCP Server.

    This function returns the pre-configured app from http_server.
    The app is already initialized with all routes, middleware, and dependencies.

    Args:
        include_cors: Whether CORS middleware is included (default: True, already in app)
        include_static: Whether static files are mounted (default: True, already in app)

    Returns:
        Configured FastAPI application instance

    Example:
        # Standalone usage
        app = create_app()

        # Mount in another app with prefix
        from simplemem_mcp import create_app
        main_app = FastAPI()
        mcp_app = create_app()
        main_app.mount("/simplemem", mcp_app)

    Note:
        The app is configured via environment variables. See README_PACKAGE.md
        for configuration details.
    """
    # For now, we return the default app
    # In the future, we could support customization by rebuilding the app
    # with different settings, but that would require significant refactoring
    return _default_app


__all__ = ["create_app"]
