from fastapi import FastAPI
from simplemem_mcp import create_app
import uvicorn

# Create your main application
app = FastAPI(
    title="My AI Application", description="Application with integrated memory service"
)


# Add your own routes
@app.get("/")
async def root():
    return {"message": "Welcome to my AI application"}


@app.get("/health")
async def health():
    return {"status": "healthy"}


# Mount SimpleMem MCP under /memory prefix
mcp_app = create_app()
app.mount("/memory", mcp_app)

# Run the combined application
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
