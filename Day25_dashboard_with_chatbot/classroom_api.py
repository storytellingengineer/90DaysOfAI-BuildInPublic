import os
import io
from datetime import datetime
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from PyPDF2 import PdfReader

from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

# FINAL ALTERNATIVE SCOPES LIST
# Using the scope that is available in your Google Cloud Console.
SCOPES = sorted([
    "https://www.googleapis.com/auth/classroom.courses.readonly",
    "https://www.googleapis.com/auth/classroom.course-work.readonly",
    "https://www.googleapis.com/auth/classroom.student-submissions.me.readonly",
    "https://www.googleapis.com/auth/drive.readonly"
])

def get_classroom_service():
    """Authenticates with Google and returns Classroom and Drive service objects."""
    creds = None
    creds_path = 'credentials.json'
    token_path = 'token.json'

    if os.path.exists(token_path):
        try:
            creds = Credentials.from_authorized_user_file(token_path, SCOPES)
        except Exception:
            os.remove(token_path)
            creds = None

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            try:
                creds.refresh(Request())
            except Exception:
                os.remove(token_path)
                flow = InstalledAppFlow.from_client_secrets_file(creds_path, SCOPES)
                creds = flow.run_local_server(port=0)
        else:
            flow = InstalledAppFlow.from_client_secrets_file(creds_path, SCOPES)
            creds = flow.run_local_server(port=0)
        
        with open(token_path, 'w') as token:
            token.write(creds.to_json())

    print("✅ Google Authentication Successful.")
    classroom = build('classroom', 'v1', credentials=creds)
    drive = build('drive', 'v3', credentials=creds)
    return classroom, drive

def fetch_assignments(classroom, course_name_keyword=""):
    """Fetches all assignments and their submission status for the user."""
    print("Fetching courses...")
    courses = classroom.courses().list().execute().get('courses', [])
    assignments = []

    if not courses:
        print("No courses found.")
        return assignments

    print(f"Found {len(courses)} courses. Searching for assignments...")
    for course in courses:
        if course_name_keyword.lower() not in course['name'].lower():
            continue
        
        course_id = course['id']
        coursework_response = classroom.courses().courseWork().list(courseId=course_id).execute()
        coursework = coursework_response.get('courseWork', [])
        
        if not coursework:
            continue

        print(f"  > Found {len(coursework)} assignments in course: {course['name']}")
        for work in coursework:
            submissions = classroom.courses().courseWork().studentSubmissions().list(
                courseId=course_id,
                courseWorkId=work['id'],
                userId='me'
            ).execute().get('studentSubmissions', [])

            submission_state = 'Not Submitted'
            if submissions:
                state = submissions[0].get('state')
                if state == 'TURNED_IN':
                    submission_state = 'Submitted'
                elif state == 'RETURNED':
                    submission_state = 'Graded and Returned'
                elif state == 'RECLAIMED_BY_STUDENT':
                    submission_state = 'Reclaimed by Student'

            assignments.append({
                'course': course['name'],
                'title': work.get('title'),
                'description': work.get('description', ''),
                'due': work.get('dueDate', {}),
                'attachments': work.get('materials', []),
                'course_id': course_id,
                'work_id': work['id'],
                'submission_state': submission_state
            })
    print(f"✅ Total assignments fetched: {len(assignments)}")
    return assignments

def extract_text_from_drive_pdf(drive, file_id):
    """Downloads a PDF from Google Drive and extracts its text."""
    try:
        request = drive.files().get_media(fileId=file_id)
        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while not done:
            status, done = downloader.next_chunk()
        fh.seek(0)
        reader = PdfReader(fh)
        text = "\n".join(page.extract_text() or "" for page in reader.pages)
        return text
    except Exception as e:
        print(f"⚠️ Could not read PDF with file_id {file_id}. Error: {e}")
        return ""

def build_vector_store(drive, assignments):
    """Builds a FAISS vector store from assignment details and PDF attachments."""
    docs = []
    print("Processing assignments for chatbot...")

    for assign in assignments:
        due_date = assign.get('due', {})
        if due_date:
            formatted_due = f"{due_date.get('year', 'N/A')}-{due_date.get('month', 'N/A'):02d}-{due_date.get('day', 'N/A'):02d}"
        else:
            formatted_due = "No due date specified"

        content = (
            f"Assignment Title: {assign['title']}\n"
            f"Course: {assign['course']}\n"
            f"Due Date: {formatted_due}\n"
            f"Submission Status: {assign.get('submission_state', 'N/A')}\n\n"
            f"Instructions:\n{assign.get('description', 'No description provided.')}"
        )
        metadata = {"course": assign["course"], "title": assign["title"], "source": "Assignment Description"}
        docs.append(Document(page_content=content, metadata=metadata))

    for assign in assignments:
        for mat in assign.get('attachments', []):
            if 'driveFile' not in mat:
                continue
            try:
                drive_file = mat['driveFile']['driveFile']
                file_id = drive_file['id']
                file_title = drive_file.get('title', '')
                
                if file_title.lower().endswith('.pdf'):
                    print(f"  > Reading PDF: {file_title}")
                    text = extract_text_from_drive_pdf(drive, file_id)
                    if text:
                        metadata = {"course": assign["course"], "title": assign["title"], "source": f"PDF: {file_title}"}
                        docs.append(Document(page_content=text, metadata=metadata))
            except Exception as e:
                print(f"⚠️ Error processing attachment: {e}")

    if not docs:
        print("No documents were created. Vector store will be empty.")
        return None

    print("Splitting documents and creating embeddings...")
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    all_chunks = splitter.split_documents(docs)

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(all_chunks, embedding=embeddings)
    print("✅ Vector store built successfully.")
    return vectorstore