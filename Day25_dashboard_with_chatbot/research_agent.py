# research_agent.py
import os
from aiohttp import web, ClientSession
from dotenv import load_dotenv
import google.generativeai as genai

# --- NEW: Added API Key Configuration for consistency and future use ---
load_dotenv()
try:
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model = genai.GenerativeModel("gemini-1.5-flash")
    print("RESEARCH_AGENT: Gemini model configured successfully for future use.")
except Exception as e:
    # This is not fatal for this agent yet, as it only uses the MCP tool.
    print(f"WARNING: Research agent could not configure Gemini. Summarization will not work. Error: {e}")
    model = None
# ---------------------------------------------------------------------

MCP_SERVER_URL = "http://localhost:8081"

async def invoke(request):
    data = await request.json()
    topic = data.get("topic")
    print(f"RESEARCH_AGENT: Received topic to research: {topic}")

    # This agent calls the MCP server to use a 'web_search_tool'
    async with ClientSession() as session:
        # NOTE: For now, we are just returning the raw result.
        # In the future, you could use the configured 'model' to summarize this result.
        payload = {"tool_name": "web_search_tool", "parameters": {"query": topic}}
        async with session.post(f"{MCP_SERVER_URL}/use_tool", json=payload) as resp:
            search_result = await resp.json()

    return web.json_response({"summary": search_result.get("result")})

app = web.Application()
app.router.add_post("/invoke", invoke)

if __name__ == "__main__":
    print("Starting Research Agent on http://localhost:8085")
    web.run_app(app, port=8085)