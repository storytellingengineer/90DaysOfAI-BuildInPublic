from fastapi import APIRouter
from schemas import GenerateRequest
from services.llm_service import generate_cover_letter
from services.history_service import save_to_db

router = APIRouter()

@router.post("/api/generate-cover-letter")
async def generate_letter(request: GenerateRequest):

    with open("prompts/gold_standard_prompt.txt", "r") as f:
        system_prompt = f.read()

    letter = generate_cover_letter(
        request.resume_text,
        request.job_description,
        system_prompt
    )

    await save_to_db(request.resume_text, request.job_description, letter)

    return {
        "cover_letter": letter
    }