# Using SimpleMem MCP from Git Repository

This guide shows how to install and use SimpleMem MCP in your other projects after pushing it to a Git repository.

## Installation from Git

### Option 1: Install from GitHub/GitLab (Recommended)

Once you push the MCP folder to a Git repository, install it in your other project:

```bash
# Install from GitHub
pip install git+https://github.com/yourusername/SimpleMem.git#subdirectory=MCP

# Or from GitLab
pip install git+https://gitlab.com/yourusername/SimpleMem.git#subdirectory=MCP

# Or from a private repo with SSH
pip install git+ssh://git@github.com/yourusername/SimpleMem.git#subdirectory=MCP
```

**Note:** The `#subdirectory=MCP` part is important because the package is in the MCP subfolder.

### Option 2: Install from Local Path (Development)

For local development/testing:

```bash
pip install -e /path/to/SimpleMem/MCP
```

## Usage in Your Other Project

### Example 1: Basic Integration

**File: `your_project/main.py`**

```python
from fastapi import FastAPI
from simplemem_mcp import create_app
import uvicorn

# Your main application
app = FastAPI(title="My Application")

# Your routes
@app.get("/")
async def root():
    return {"message": "Hello World"}

# Mount SimpleMem MCP
mcp_app = create_app()
app.mount("/memory", mcp_app)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

### Example 2: With Environment Configuration

**File: `your_project/.env`**

```bash
# SimpleMem MCP Configuration
JWT_SECRET_KEY=your-secret-key-here
ENCRYPTION_KEY=your-base64-encoded-32-byte-key

# LLM Provider
LLM_PROVIDER=litellm
LITELLM_BASE_URL=https://your-litellm-proxy.com
LITELLM_LLM_MODEL=gpt-4
LITELLM_EMBEDDING_MODEL=text-embedding-3-small
EMBEDDING_DIMENSION=1536

# Database paths (relative to your project)
USER_DB_PATH=./data/users.db
LANCEDB_PATH=./data/lancedb
```

**File: `your_project/main.py`**

```python
from fastapi import FastAPI
from simplemem_mcp import create_app
import uvicorn
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI()

# Your routes
@app.get("/")
async def root():
    return {"status": "ok"}

@app.get("/api/chat")
async def chat():
    # Your chat logic here
    return {"response": "Hello"}

# Mount SimpleMem MCP under /memory
mcp_app = create_app()
app.mount("/memory", mcp_app)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

### Example 3: Multiple Prefixes

You can even mount multiple instances with different configurations:

```python
from fastapi import FastAPI
from simplemem_mcp import create_app

app = FastAPI()

# Mount for user memories
user_mcp = create_app()
app.mount("/user-memory", user_mcp)

# Mount for system memories (if you want separate instances)
system_mcp = create_app()
app.mount("/system-memory", system_mcp)
```

## Project Structure

Your other project would look like:

```
your-project/
├── .env                    # Environment configuration
├── requirements.txt        # Dependencies
├── main.py                # Your application
├── data/                  # SimpleMem data (auto-created)
│   ├── users.db
│   └── lancedb/
└── your_app/
    ├── __init__.py
    └── routes.py
```

**File: `your-project/requirements.txt`**

```txt
fastapi>=0.109.0
uvicorn[standard]>=0.27.0
python-dotenv>=1.0.0

# Install SimpleMem MCP from Git
git+https://github.com/yourusername/SimpleMem.git#subdirectory=MCP
```

Then install with:
```bash
pip install -r requirements.txt
```

## Available Endpoints

After mounting at `/memory`, all MCP routes are available:

- `POST /memory/api/auth/register` - Register new user
- `GET /memory/api/auth/verify` - Verify token
- `POST /memory/api/auth/refresh` - Refresh token
- `GET /memory/api/health` - Health check
- `GET /memory/api/server/info` - Server info
- `POST /memory/mcp` - MCP protocol endpoint
- `GET /memory/mcp` - MCP SSE stream
- `DELETE /memory/mcp` - Terminate session

## Testing Your Integration

```bash
# Start your server
python main.py

# Test your routes
curl http://localhost:8000/

# Test SimpleMem routes
curl http://localhost:8000/memory/api/health

# Register a user
curl -X POST http://localhost:8000/memory/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{"litellm_api_key": "your-key"}'
```

## Git Repository Setup

### Step 1: Push to Git

```bash
cd /Users/darshan.sithan/Documents/simpleMemFork/SimpleMem
git add MCP/
git commit -m "Add SimpleMem MCP package"
git push origin main
```

### Step 2: In Your Other Project

```bash
# Clone your other project
cd /path/to/your-other-project

# Install SimpleMem MCP
pip install git+https://github.com/yourusername/SimpleMem.git#subdirectory=MCP

# Or add to requirements.txt
echo "git+https://github.com/yourusername/SimpleMem.git#subdirectory=MCP" >> requirements.txt
pip install -r requirements.txt
```

### Step 3: Use It

```python
from simplemem_mcp import create_app

# That's it! The package is installed and ready to use
```

## Important Notes

1. **Python Version**: Requires Python 3.10+ (due to `mcp` package dependency)

2. **Environment Variables**: Make sure to set all required environment variables in your other project

3. **Data Directories**: The `USER_DB_PATH` and `LANCEDB_PATH` will be created relative to where you run your application

4. **Dependencies**: All SimpleMem dependencies will be installed automatically when you install the package

5. **Updates**: To update SimpleMem MCP in your project:
   ```bash
   pip install --upgrade git+https://github.com/yourusername/SimpleMem.git#subdirectory=MCP
   ```
