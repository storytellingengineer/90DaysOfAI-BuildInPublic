"# AI Cover Letter Architect 🎯

A production-ready, AI-powered web application that generates highly personalized, professional cover letters. Built with React, FastAPI, and OpenAI GPT-4o.

![AI Cover Letter Architect](https://img.shields.io/badge/Status-Production_Ready-success)
![React](https://img.shields.io/badge/React-19.0-61DAFB?logo=react)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110-009688?logo=fastapi)
![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python)

## 🌟 Features

- **Smart PDF Parsing**: Upload your resume in PDF format and extract text automatically using PyMuPDF
- **AI-Powered Generation**: Leverages OpenAI GPT-4o to craft compelling, natural-sounding cover letters
- **Senior Recruiter Persona**: AI acts as an experienced talent acquisition specialist, focusing on quantifiable achievements and cultural fit
- **Multiple Export Formats**: Download your cover letter as PDF or DOCX
- **Professional UI**: Swiss Organic design system with Playfair Display, Inter, and Cormorant Garamond typography
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices
- **Copy to Clipboard**: Quickly copy your generated cover letter
- **History Tracking**: All generated letters are stored in MongoDB for future reference

## 🎨 Design Philosophy

The app follows a \"Swiss Organic\" design system:
- **Typography**: Playfair Display for headings, Inter for UI, Cormorant Garamond for letter display
- **Colors**: Paper White (#FAFAFA), Slate Black (#0F172A), International Klein Blue (#002FA7)
- **Layout**: Split-pane architecture (40% input context, 60% creation canvas)
- **Aesthetics**: Clean, professional, with generous spacing and subtle shadows

## 🚀 Tech Stack

### Backend
- **FastAPI**: High-performance Python web framework
- **PyMuPDF (fitz)**: Robust PDF text extraction
- **OpenAI GPT-4o**: LLM integration via emergentintegrations library
- **MongoDB**: Document storage with Motor async driver
- **python-docx**: DOCX file generation
- **reportlab**: PDF document creation

### Frontend
- **React 19**: Modern UI library
- **Tailwind CSS**: Utility-first styling
- **react-dropzone**: Drag-and-drop file upload
- **jsPDF**: Client-side PDF generation
- **docx.js**: Client-side DOCX generation
- **Sonner**: Beautiful toast notifications
- **Lucide React**: Icon library

## 📁 Project Structure

```
/app
├── backend/
│   ├── server.py           # Main FastAPI application
│   ├── requirements.txt    # Python dependencies
│   └── .env                # Environment variables
├── frontend/
│   ├── src/
│   │   ├── App.js          # Main React component
│   │   ├── App.css         # Custom styles
│   │   ├── index.css       # Global styles with design tokens
│   │   └── components/ui/  # Shadcn UI components
│   ├── public/
│   │   └── index.html      # HTML template with Google Fonts
│   ├── package.json        # Node dependencies
│   └── tailwind.config.js  # Tailwind configuration
└── README.md
```

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.11+
- Node.js 18+
- MongoDB (local or cloud)
- OpenAI API key or Emergent LLM key

### Backend Setup

1. **Install Python dependencies**:
```bash
cd backend
pip install -r requirements.txt
```

2. **Configure environment variables**:
Create a `.env` file in the `backend` directory:
```env
MONGO_URL=\"mongodb://localhost:27017\"
DB_NAME=\"cover_letter_db\"
CORS_ORIGINS=\"*\"
EMERGENT_LLM_KEY=your_api_key_here
```

3. **Run the backend**:
```bash
uvicorn server:app --host 0.0.0.0 --port 8001 --reload
```

### Frontend Setup

1. **Install dependencies**:
```bash
cd frontend
yarn install
```

2. **Configure environment variables**:
Create a `.env` file in the `frontend` directory:
```env
REACT_APP_BACKEND_URL=http://localhost:8001
```

3. **Run the frontend**:
```bash
yarn start
```

The app will be available at `http://localhost:3000`

## 🔑 API Endpoints

### `POST /api/upload-resume`
Upload and parse a PDF resume.

**Request**: multipart/form-data with `file` field
**Response**:
```json
{
  \"success\": true,
  \"resume_text\": \"Extracted resume text...\",
  \"filename\": \"resume.pdf\"
}
```

### `POST /api/generate-cover-letter`
Generate a personalized cover letter.

**Request**:
```json
{
  \"resume_text\": \"Your resume content...\",
  \"job_description\": \"Job posting details...\"
}
```

**Response**:
```json
{
  \"cover_letter\": \"Generated cover letter...\",
  \"generated_at\": \"2025-01-20T10:30:00Z\"
}
```

### `POST /api/download-pdf`
Download cover letter as PDF.

**Request**:
```json
{
  \"cover_letter\": \"Letter text...\"
}
```

**Response**: PDF file download

### `POST /api/download-docx`
Download cover letter as DOCX.

**Request**:
```json
{
  \"cover_letter\": \"Letter text...\"
}
```

**Response**: DOCX file download

### `GET /api/history`
Retrieve generation history (last 10 letters).

## 🎯 The \"Gold Standard\" Prompt

The AI uses a carefully crafted system prompt that instructs it to act as a **Senior Talent Acquisition Specialist** with 15+ years of experience. Key principles:

1. **No generic openings**: Avoids phrases like \"I am writing to express my interest...\"
2. **Hook-first approach**: Starts with a compelling story or achievement
3. **Specificity**: Uses metrics and concrete examples from the resume
4. **Natural tone**: Writes conversationally, not like typical AI
5. **Concise**: 3-4 paragraphs, max 350 words
6. **Value-focused closing**: Reinforces candidate value, not generic thanks

## 🚢 Deployment

### Deploy Backend (Render.com)

1. Create a new Web Service on [Render](https://render.com)
2. Connect your GitHub repository
3. Configure:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn server:app --host 0.0.0.0 --port $PORT`
4. Add environment variables (MONGO_URL, DB_NAME, EMERGENT_LLM_KEY)
5. Deploy!

### Deploy Frontend (Vercel)

1. Push your code to GitHub
2. Import project on [Vercel](https://vercel.com)
3. Configure:
   - **Framework Preset**: Create React App
   - **Root Directory**: `frontend`
   - **Build Command**: `yarn build`
   - **Output Directory**: `build`
4. Add environment variable:
   - `REACT_APP_BACKEND_URL`: Your backend URL
5. Deploy!

### Alternative: Railway

Both frontend and backend can be deployed on [Railway](https://railway.app) with automatic GitHub deployments.

## 🧪 Testing

Backend API tests:
```bash
curl -X POST http://localhost:8001/api/generate-cover-letter \
  -H \"Content-Type: application/json\" \
  -d '{
    \"resume_text\": \"Your resume...\",
    \"job_description\": \"Job description...\"
  }'
```

## 📊 Database Schema

**Collection**: `cover_letters`
```javascript
{
  id: String,              // UUID
  resume_text: String,     // Truncated (first 1000 chars)
  job_description: String, // Truncated (first 1000 chars)
  cover_letter: String,    // Full generated letter
  generated_at: DateTime   // ISO timestamp
}
```

## 🎓 Key Learnings & Best Practices

1. **PDF Parsing**: PyMuPDF (fitz) is more reliable than pdfplumber for complex PDFs
2. **LLM Prompting**: Specific system prompts with clear instructions produce better results
3. **Error Handling**: Always validate inputs (minimum length, file types)
4. **File Generation**: Server-side (python-docx, reportlab) gives more control than client-side
5. **Design System**: Defining typography and color tokens upfront ensures consistency

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- OpenAI for GPT-4o
- Emergent.sh for LLM integration infrastructure
- Shadcn UI for beautiful React components
- The PyMuPDF team for excellent PDF parsing

## 📧 Contact

For questions or feedback, please open an issue on GitHub.

---

**Made with ❤️ using Emergent**
"