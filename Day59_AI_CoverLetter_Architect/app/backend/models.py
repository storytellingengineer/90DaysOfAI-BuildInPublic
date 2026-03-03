from datetime import datetime
import uuid

def create_cover_letter_document(resume_text, job_description, cover_letter):
    return {
        "id": str(uuid.uuid4()),
        "resume_text": resume_text[:1000],
        "job_description": job_description[:1000],
        "cover_letter": cover_letter,
        "generated_at": datetime.utcnow()
    }