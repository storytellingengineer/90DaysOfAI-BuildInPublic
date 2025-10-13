# planner_agent.py
import os
from aiohttp import web
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
try:
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model = genai.GenerativeModel("gemini-1.5-flash")
    print("PLANNER_AGENT: Gemini model configured successfully.")
except Exception as e:
    print(f"FATAL: Planner agent could not configure Gemini. Is GEMINI_API_KEY set? Error: {e}")
    model = None

# --- NEW, MORE POWERFUL PLANNING PROMPT ---
PLANNING_PROMPT = """
You are an expert academic planner and learning strategist. Your job is to create a specific, actionable study plan based on the user's goals and current workload.

**Context:**
1.  **User's Current Workload / Pending Assignments:**
    {task_list}

2.  **User's Specific Learning Goal for Today:**
    {learning_goal}

**Your Task:**
- If a specific `learning_goal` is provided, create a detailed, step-by-step plan for the user to learn that topic. Include estimated times and suggest activities like "initial research," "watch a tutorial," "practical implementation," and "review."
- If the `learning_goal` is "None" or empty, and there are pending assignments, create a plan to complete those assignments.
- If the `learning_goal` is "None" AND there are no pending assignments, then and only then should you create a generic "proactive enhancement" plan.
- Make the plan encouraging and specific. Address the user's goal directly in your response.
"""

async def invoke(request):
    if not model:
        return web.json_response({"error": "Planner agent's AI model is not initialized."}, status=500)

    # The orchestrator will now send a dictionary with more context
    data = await request.json()
    task_list = data.get("task_list", "No information on pending tasks.")
    learning_goal = data.get("learning_goal", "None")
    
    print(f"PLANNER_AGENT: Received request to plan for topic '{learning_goal}' with workload: '{task_list[:100]}...'")
    
    prompt = PLANNING_PROMPT.format(task_list=task_list, learning_goal=learning_goal)
    response = model.generate_content(prompt)
    
    return web.json_response({"plan": response.text})

app = web.Application()
app.router.add_post("/invoke", invoke)

if __name__ == "__main__":
    print("Starting Planner Agent on http://localhost:8084")
    web.run_app(app, port=8084)