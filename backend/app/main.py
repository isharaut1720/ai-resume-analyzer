
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.resume_parser import extract_text
from app.job_matcher import match_jobs
from app.ai_suggestions import get_suggestions, calculate_ats_score


app = FastAPI(
    title="AI Career Assistant",
    description="Resume Analyzer and Job Recommendation System",
    version="1.0.0"
)


# CORS CONFIGURATION
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


# HOME ROUTE
@app.get("/")
def root():
    return {
        "message": "AI Career Assistant Backend is running successfully!"
    }


# HEALTH CHECK
@app.get("/health")
def health_check():
    return {"status": "healthy"}


# RESUME ANALYSIS
@app.post("/analyze/")
async def analyze_resume(file: UploadFile = File(...)):

    # Check file type
    if not file.filename or not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    try:
        # Extract resume text
        text = await extract_text(file)

        # Match jobs
        jobs = match_jobs(text)

        # Generate suggestions
        suggestions = get_suggestions(text)

        # Calculate ATS score
        ats_score = calculate_ats_score(text)

        return {
            "success": True,
            "jobs": jobs,
            "suggestions": suggestions,
            "ats_score": ats_score
        }

    except HTTPException:
        raise

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Something went wrong while analyzing the resume."
        )

    finally:
        await file.close()
