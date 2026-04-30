from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

from app.resume_parser import extract_text
from app.job_matcher import match_jobs
from app.ai_suggestions import get_suggestions, calculate_ats_score

app = FastAPI()

# ✅ CORS (FIXED)
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "https://ai-resume-analyzer-isha-2026.netlify.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ OPTIONAL: root route (so "/" doesn't show Not Found)
@app.get("/")
def root():
    return {"message": "Backend is running 🚀"}

@app.post("/analyze/")
async def analyze_resume(file: UploadFile = File(...)):
    try:
        text = await extract_text(file)

        jobs = match_jobs(text)
        suggestions = get_suggestions(text)
        ats_score = calculate_ats_score(text)

        return {
            "jobs": jobs,
            "suggestions": suggestions,
            "ats_score": ats_score
        }

    except Exception as e:
        return {"error": str(e)}