# orchestrator_agent.py
import os
import json
from aiohttp import web, ClientSession
from dotenv import load_dotenv
import google.generativeai as genai

# --- Configuration & Initialization ---
load_dotenv()
try:
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model = genai.GenerativeModel("gemini-1.5-flash-latest")
except Exception as e:
    print(f"FATAL: Could not configure Gemini. Is GEMINI_API_KEY set correctly? Error: {e}")
    model = None

# Agent Endpoints
TUTOR_AGENT_URL = "http://localhost:8083/invoke"
PLANNER_AGENT_URL = "http://localhost:8084/invoke"
RESEARCH_AGENT_URL = "http://localhost:8085/invoke"

# --- CORRECTED ROUTING PROMPT ---
# The literal curly braces for the JSON examples are now "escaped" by doubling them up ({{ and }}).
# The one real placeholder {user_request} remains with single braces.
ROUTING_PROMPT = """
You are the central dispatcher for a team of AI agents. Your job is to analyze the user's request and decide which agent is best suited to handle it.
You must respond in JSON format.

Here are the available agents:
- "planner": Use this agent for requests related to creating schedules, making plans, or managing time.
- "tutor": Use this agent for specific questions about the user's assignments, courses, due dates, or content within their documents. This is the primary knowledge base agent.
- "researcher": Use this agent for general knowledge questions or requests to find new information on the web.

User Request: "{user_request}"

Analyze the request and determine the correct agent and the precise query to send to that agent.

Your JSON response must have two keys:
1. "agent_to_use": One of ["planner", "tutor", "researcher", "unknown"].
2. "query_for_agent": The user's original request, or a simplified version of it for the agent.

Example 1:
User Request: "Plan my day to get my pending tasks done"
Your JSON response:
{{
  "agent_to_use": "planner",
  "query_for_agent": "What are all my pending assignments?"
}}

Example 2:
User Request: "help me submit the assignment 6, when is it due"
Your JSON response:
{{
  "agent_to_use": "tutor",
  "query_for_agent": "When is assignment 6 due and what are its details?"
}}

Example 3:
User Request: "Who was the first president of the USA?"
Your JSON response:
{{
  "agent_to_use": "researcher",
  "query_for_agent": "Who was the first president of the USA?"
}}
"""

# In orchestrator_agent.py, replace the invoke function with this one.

async def invoke(request):
    """
    This is the main entry point. It receives the user's goal, uses an LLM to decide
    which agent to use, and then routes the request to that agent with proper context.
    """
    if not model:
        return web.json_response({"final_answer": "Error: The Orchestrator's AI model is not initialized. Check the API key."}, status=500)

    data = await request.json()
    user_goal = data.get("goal")
    if not user_goal:
        return web.json_response({"error": "User goal not provided."}, status=400)

    print(f"ORCHESTRATOR: Received goal: '{user_goal}'")
    
    response_text_for_logging = "Not yet generated"
    try:
        # Step 1: LLM call and routing decision
        prompt = ROUTING_PROMPT.format(user_request=user_goal)
        
        try:
            response = await model.generate_content_async(prompt)
            response_text_for_logging = response.text
        except Exception as model_call_error:
            # Handle errors during the API call
            print(f"--- ORCHESTRATOR CRITICAL ERROR: The call to the Gemini model failed. ---")
            print(f"Error Type: {type(model_call_error)}")
            print(f"Error Representation: {repr(model_call_error)}")
            raise model_call_error

        json_start = response_text_for_logging.find('{')
        json_end = response_text_for_logging.rfind('}') + 1
        if json_start == -1 or json_end == 0: raise ValueError("No valid JSON object found in the LLM response.")
        clean_json_str = response_text_for_logging[json_start:json_end]
        decision = json.loads(clean_json_str)
        
        agent_to_use = decision.get("agent_to_use")
        query_for_agent = decision.get("query_for_agent")
        
        print(f"ORCHESTRATOR: Routing decision: Use '{agent_to_use}' with query: '{query_for_agent}'")

    except Exception as e:
        print(f"--- ORCHESTRATOR CRITICAL ERROR in routing phase ---")
        print(f"LLM Raw Response Text: {response_text_for_logging}")
        print(f"Caught Exception Type: {type(e)}")
        print(f"Caught Exception Representation: {repr(e)}")
        print(f"----------------------------------------------------")
        return web.json_response({"final_answer": "I encountered a problem while trying to understand your request. Please try rephrasing your question."}, status=500)
    
    # Step 2: Route the request to the chosen agent.
    final_response = "I'm not sure how to handle that request."
    async with ClientSession() as session:
        try:
            if agent_to_use == "tutor":
                payload = {"task": "answer_query", "query": query_for_agent}
                async with session.post(TUTOR_AGENT_URL, json=payload) as resp:
                    resp.raise_for_status()
                    final_response = (await resp.json()).get("answer", "The tutor agent had no answer.")

            # --- THIS IS THE NEW, CORRECTED LOGIC FOR THE PLANNER ---
            elif agent_to_use == "planner":
                print("ORCHESTRATOR: Beginning specific plan generation...")
                
                # 1. Get the current workload from the Tutor Agent
                tutor_payload = {"task": "answer_query", "query": "What are all my pending assignments?"}
                print(f"ORCHESTRATOR: -> Asking Tutor Agent for current workload.")
                async with session.post(TUTOR_AGENT_URL, json=tutor_payload) as tutor_resp:
                    tutor_resp.raise_for_status()
                    task_list = (await tutor_resp.json()).get("answer")
                
                # 2. Get the specific learning goal from the initial user query
                # The 'query_for_agent' from our router now contains the user's specific goal.
                learning_goal = query_for_agent

                # 3. Send BOTH pieces of information to the Planner Agent
                print(f"ORCHESTRATOR: -> Asking Planner Agent to create a plan.")
                planner_payload = {
                    "task_list": task_list,
                    "learning_goal": learning_goal
                }
                async with session.post(PLANNER_AGENT_URL, json=planner_payload) as planner_resp:
                    planner_resp.raise_for_status()
                    final_response = (await planner_resp.json()).get("plan", "The planner agent failed to create a plan.")
            # --------------------------------------------------------
            
            elif agent_to_use == "researcher":
                payload = {"topic": query_for_agent}
                async with session.post(RESEARCH_AGENT_URL, json=payload) as resp:
                    resp.raise_for_status()
                    final_response = (await resp.json()).get("summary", "The researcher agent found nothing.")

        except Exception as e:
            error_msg = f"ORCHESTRATOR: Error communicating with downstream agent '{agent_to_use}'. Error: {e}"
            print(error_msg)
            final_response = f"Sorry, there was an error contacting the {agent_to_use}. Please check its server logs."

    return web.json_response({"final_answer": final_response})


app = web.Application()
app.router.add_post("/invoke", invoke)

if __name__ == "__main__":
    print("Starting Intelligent Orchestrator Agent on http://localhost:8086")
    web.run_app(app, port=8086)