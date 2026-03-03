from emergentintegrations.llm.chat import Chat
from config import settings

def generate_cover_letter(resume_text, job_description, system_prompt):

    chat = Chat(
        api_key=settings.EMERGENT_LLM_KEY,
        model="gpt-4o"
    )

    chat.add_message("system", system_prompt)

    chat.add_message("user", f"""
    RESUME:
    {resume_text}

    JOB DESCRIPTION:
    {job_description}
    """)

    response = chat.get_response()

    return response