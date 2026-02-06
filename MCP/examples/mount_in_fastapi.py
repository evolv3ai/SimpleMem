"""
Example: Mounting SimpleMem MCP in an existing FastAPI application

This example shows how to integrate SimpleMem MCP into your existing
FastAPI application with a custom prefix.
"""

from fastapi import FastAPI
from simplemem_mcp import create_app
import uvicorn

# Create your main FastAPI application
app = FastAPI(
    title="My AI Application",
    description="Application with integrated SimpleMem memory service",
    version="1.0.0",
)


# Your existing routes
@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Welcome to my AI application",
        "memory_service": "Available at /simplemem/*",
    }


@app.get("/api/health")
async def health():
    """Health check for main application"""
    return {"status": "healthy", "service": "main"}


@app.get("/api/features")
async def features():
    """List application features"""
    return {
        "features": ["AI Chat", "Memory Service (SimpleMem MCP)", "User Management"]
    }


# Mount SimpleMem MCP under /simplemem prefix
# All MCP routes will be available under this prefix:
# - /simplemem/api/auth/register
# - /simplemem/api/auth/verify
# - /simplemem/mcp
# - /simplemem/api/health
# etc.
mcp_app = create_app()
app.mount("/simplemem", mcp_app)

# Run the combined application
if __name__ == "__main__":
    print("Starting application with SimpleMem MCP mounted at /simplemem")
    print("Main app routes:")
    print("  - GET /")
    print("  - GET /api/health")
    print("  - GET /api/features")
    print("\nSimpleMem MCP routes (under /simplemem):")
    print("  - POST /simplemem/api/auth/register")
    print("  - GET /simplemem/api/auth/verify")
    print("  - POST /simplemem/mcp")
    print("  - GET /simplemem/api/health")
    print("  - GET /simplemem/api/server/info")

    uvicorn.run(app, host="0.0.0.0", port=8000)
