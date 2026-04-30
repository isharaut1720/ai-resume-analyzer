import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ✅ Correct dataset path (robust)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "..", "dataset", "jobs.csv")

jobs_df = pd.read_csv(DATA_PATH)

# 🔥 NEW: Skill extraction
def extract_skills(text):
    skills = [
        "python", "java", "react", "node", "sql",
        "machine learning", "html", "css", "javascript",
        "spring boot", "django", "flask", "mongodb",
        "mysql", "c++", "data science"
    ]

    found_skills = []

    for skill in skills:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    return " ".join(found_skills)


def match_jobs(resume_text):
    # 🔥 Extract only skills from resume
    resume_skills = extract_skills(resume_text)

    # If no skills found, fallback to full text
    if resume_skills.strip() == "":
        resume_skills = resume_text

    # Create corpus
    corpus = jobs_df["description"].tolist()
    corpus.append(resume_skills)

    # TF-IDF
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(corpus)

    # Cosine similarity
    similarity = cosine_similarity(vectors[-1], vectors[:-1])

    scores = list(enumerate(similarity[0]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    # 🔥 Filter low similarity + pick top 5
    top_jobs = []
    for i in scores:
        if i[1] > 0.2:   # threshold (important)
            top_jobs.append(jobs_df.iloc[i[0]]["title"])

    return top_jobs[:5]