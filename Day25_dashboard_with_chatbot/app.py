# app.py
import streamlit as st
import requests
from datetime import date, timedelta

# --- Configuration: Agent Endpoints ---
# The URL for the agent that fetches the initial data for the dashboard UI
CLASSROOM_AGENT_URL = "http://localhost:8082/invoke" 
# The URL for the main "brain" of the operation that handles complex user requests
ORCHESTRATOR_AGENT_URL = "http://localhost:8086/invoke" 

# --- Page Configuration ---
st.set_page_config(page_title="AI Academic Team Dashboard", layout="wide")

# --- App State Management ---
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "initialized" not in st.session_state:
    st.session_state.initialized = False
if "assignments_data" not in st.session_state:
    st.session_state.assignments_data = []

# --- Helper Functions (for UI Display) ---
def get_date_from_due(due_obj):
    """Safely converts Google's due date dictionary to a Python date object."""
    if due_obj and 'year' in due_obj and 'month' in due_obj and 'day' in due_obj:
        return date(due_obj['year'], due_obj['month'], due_obj['day'])
    return None

def display_assignment(assignment):
    """Renders a single assignment in the dashboard."""
    due_date = get_date_from_due(assignment.get('due'))
    due_date_str = due_date.strftime("%B %d, %Y") if due_date else "No due date"
    with st.expander(f"{assignment['title']} - (Due: {due_date_str})"):
        st.markdown(f"**Course:** {assignment['course']}")
        st.markdown(f"**Status:** {assignment['submission_state']}")
        st.markdown(f"**Instructions:**\n\n{assignment.get('description', 'No description provided.')}")

# --- Agent Communication Functions ---

def initialize_dashboard_data():
    """
    Calls the Classroom Agent to fetch raw assignment data for the visual dashboard
    and trigger the vector store build in the background.
    """
    try:
        # This single call triggers the data pipeline: UI -> Classroom Agent -> MCP -> RAG Agent
        response = requests.post(CLASSROOM_AGENT_URL)
        response.raise_for_status() # Will raise an error for 4xx/5xx responses
        data = response.json()
        return data.get("result", [])
    except requests.exceptions.RequestException as e:
        st.error(f"⚠️ **Connection Error:** Could not connect to the backend agents. Please ensure all agent servers (MCP, Classroom, RAG, etc.) are running. Details: {e}")
        return []

def get_orchestrated_response(user_goal: str):
    """
    Sends the user's high-level goal to the Orchestrator Agent and gets the final,
    well-thought-out plan or answer back.
    """
    try:
        payload = {"goal": user_goal}
        response = requests.post(ORCHESTRATOR_AGENT_URL, json=payload)
        response.raise_for_status()
        return response.json().get("final_answer", "Sorry, the AI team had trouble processing that request.")
    except requests.exceptions.RequestException as e:
        st.error(f"⚠️ **Orchestrator Error:** Could not get a response from the AI team. Details: {e}")
        return "I'm having trouble connecting to my team of specialists right now. Please try again in a moment."


# --- Main App ---
st.title("🎓 AI Academic Team")
st.markdown("Your personal AI team for planning, research, and tutoring.")

# --- Initialization Block ---
if not st.session_state.initialized:
    with st.spinner("Connecting to agents and initializing your dashboard... This may take a moment."):
        fetched_assignments = initialize_dashboard_data()
        if fetched_assignments:
            st.session_state.assignments_data = fetched_assignments
        st.session_state.initialized = True
        # Only rerun if initialization was successful
        if st.session_state.assignments_data:
            st.rerun()

# --- Main Layout (Dashboard on Left, Chatbot on Right) ---
dashboard_col, chat_col = st.columns([3, 2])

# --- LEFT COLUMN: ASSIGNMENT DASHBOARD ---
with dashboard_col:
    st.header("📋 Assignments Overview")

    if not st.session_state.assignments_data:
        st.warning("Could not load assignment data. Please check the agent server terminals for errors.")
    else:
        # The entire dashboard UI code remains the same as before.
        # It's a pure display component based on the fetched data.
        st.subheader("Filter by Due Date")
        due_dates = [get_date_from_due(a.get('due')) for a in st.session_state.assignments_data if get_date_from_due(a.get('due'))]
        min_date = min(due_dates) if due_dates else date.today()
        max_date = max(due_dates) if due_dates else date.today() + timedelta(days=30)
        filter_col1, filter_col2 = st.columns(2)
        with filter_col1:
            start_date = st.date_input("Start date", min_date, min_value=min_date, max_value=max_date)
        with filter_col2:
            end_date = st.date_input("End date", max_date, min_value=min_date, max_value=max_date)
        
        st.divider()
        filtered_assignments = [a for a in st.session_state.assignments_data if get_date_from_due(a.get('due')) is None or (start_date <= get_date_from_due(a.get('due')) <= end_date)]
        
        pending = [a for a in filtered_assignments if a.get('submission_state') not in ['Submitted', 'Graded and Returned'] and (get_date_from_due(a.get('due')) is None or get_date_from_due(a.get('due')) >= date.today())]
        past_due = [a for a in filtered_assignments if a.get('submission_state') not in ['Submitted', 'Graded and Returned'] and get_date_from_due(a.get('due')) and get_date_from_due(a.get('due')) < date.today()]
        completed = [a for a in filtered_assignments if a.get('submission_state') in ['Submitted', 'Graded and Returned']]

        if past_due:
            st.subheader("🔴 Past Due")
            for assign in sorted(past_due, key=lambda x: get_date_from_due(x.get('due')) or date.min): display_assignment(assign)
        if pending:
            st.subheader("🟡 Pending")
            for assign in sorted(pending, key=lambda x: get_date_from_due(x.get('due')) or date.max): display_assignment(assign)
        if completed:
            st.subheader("✅ Completed / Graded")
            for assign in sorted(completed, key=lambda x: get_date_from_due(x.get('due')) or date.min, reverse=True): display_assignment(assign)


# --- RIGHT COLUMN: CHATBOT INTERFACE ---
with chat_col:
    st.header("🤖 Team Manager")
    st.markdown("Give your AI team a goal. For example:")
    st.caption("*Plan my day to get my pending tasks done*")
    st.caption("*Help me research 'backpropagation in neural networks'*")
    st.caption("*Explain the main points of Assignment 4*")
    
    # Display chat history
    for role, msg in st.session_state.chat_history:
        with st.chat_message(role):
            st.markdown(msg)

    # Get user input. The key is "chat_input_main"
    user_input = st.chat_input("How can your AI team help you today?")
    if user_input:
        # Display user's message
        st.session_state.chat_history.append(("user", user_input))
        with st.chat_message("user"):
            st.markdown(user_input)
        
        # Get the orchestrated response
        with st.spinner("The AI team is working on your request..."):
            response = get_orchestrated_response(user_input)
        
        # Display the final response
        st.session_state.chat_history.append(("assistant", response))
        with st.chat_message("assistant"):
            st.markdown(response)