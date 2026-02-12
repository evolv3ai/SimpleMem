curl --location 'http://localhost:8000/api/auth/register' \
--header 'Content-Type: application/json' \
--data '{
    "litellm_api_key": "sk-<>"
}'

{
  "mcpServers": {
    "simplemem": {
      "type": "http",
      "url": "http://localhost:8000/mcp",
      "headers": {
        "Authorization": "Bearer "
      }
    }
  }
}


export LITELLM_EMBEDDING_MODEL=gemini-embedding-001
export LITELLM_URL=<>
export LITELLM_MODEL=glm-latest
export EMBEDDING_DIMENSION=3072
export LLM_PROVIDER=litellm


# List all users in the database
sqlite3 MCP/data/users.db "SELECT * FROM users;" -header -column
