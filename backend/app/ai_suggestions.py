
import re


# ==========================================
# 1. ATS SCORE CALCULATION
# ==========================================

def calculate_ats_score(resume_text):

    text = resume_text.lower()

    score = 0
    total_checks = 7

    # CHECK 1: Contact Information

    email_pattern = r'[\w.+-]+@[\w.-]+\.[a-zA-Z]{2,}'
    phone_pattern = r'(\+?\d[\d\s()-]{8,}\d)'

    has_email = bool(re.search(email_pattern, resume_text))
    has_phone = bool(re.search(phone_pattern, resume_text))

    if has_email or has_phone:
        score += 1


    # CHECK 2: Education

    education_keywords = [
        "education", "bachelor", "b.tech",
        "b.e.", "degree", "university",
        "college", "graduation", "diploma",
        "bsc", "msc", "master"
    ]

    if any(word in text for word in education_keywords):
        score += 1


    # CHECK 3: Technical Skills

    technical_skills = [
        "python", "java", "javascript",
        "react", "html", "css", "sql",
        "machine learning", "c++",
        "spring boot", "django", "flask"
    ]

    detected_skills = [
        skill for skill in technical_skills
        if re.search(
            r'(?<!\w)' + re.escape(skill) + r'(?!\w)',
            text
        )
    ]

    if len(detected_skills) >= 2:
        score += 1


    # CHECK 4: Work Experience

    experience_keywords = [
        "internship", "work experience",
        "professional experience",
        "employment history",
        "work history"
    ]

    if any(word in text for word in experience_keywords):
        score += 1


    # CHECK 5: Projects

    if re.search(r'\bprojects?\b', text):
        score += 1


    # CHECK 6: Achievements

    achievement_keywords = [
        "achievement", "achievements",
        "award", "certification",
        "improved", "increased",
        "optimized", "accomplishment"
    ]

    if any(word in text for word in achievement_keywords):
        score += 1


    # CHECK 7: Technical Tools

    tools = [
        "github", "docker", "aws",
        "azure", "tableau", "power bi",
        "excel", "linux", "jenkins"
    ]

    detected_tools = [
        tool for tool in tools
        if re.search(
            r'(?<!\w)' + re.escape(tool) + r'(?!\w)',
            text
        )
    ]

    if detected_tools:
        score += 1


    # FINAL SCORE

    final_score = round((score / total_checks) * 100)

    return final_score


# ==========================================
# 2. RESUME IMPROVEMENT SUGGESTIONS
# ==========================================

def get_suggestions(resume_text):

    text = resume_text.lower()

    skills = []
    missing_skills = []
    improvements = []
    roles = []


    # TECHNICAL SKILLS

    skill_list = [
        "python", "java", "c++", "react",
        "node", "sql", "html", "css",
        "javascript", "machine learning",
        "data analysis", "spring boot",
        "django", "flask"
    ]

    for skill in skill_list:

        pattern = r'(?<!\w)' + re.escape(skill) + r'(?!\w)'

        if re.search(pattern, text):
            skills.append(skill)
        else:
            missing_skills.append(skill)


    # CONTACT INFORMATION

    email_pattern = r'[\w.+-]+@[\w.-]+\.[a-zA-Z]{2,}'
    phone_pattern = r'(\+?\d[\d\s()-]{8,}\d)'

    if not re.search(email_pattern, resume_text):
        improvements.append(
            "Add a professional email address."
        )

    if not re.search(phone_pattern, resume_text):
        improvements.append(
            "Add your contact number."
        )


    # PROJECTS

    if not re.search(r'\bprojects?\b', text):
        improvements.append(
            "Add 2-3 relevant projects with descriptions and technologies used."
        )


    # EXPERIENCE

    if not any(word in text for word in [
        "internship", "work experience",
        "professional experience"
    ]):
        improvements.append(
            "Include internship, practical training, or relevant experience if available."
        )


    # ACHIEVEMENTS

    if not any(word in text for word in [
        "achievement", "award",
        "certification", "accomplishment"
    ]):
        improvements.append(
            "Include relevant certifications, awards, or achievements."
        )


    # EDUCATION

    if not any(word in text for word in [
        "education", "bachelor",
        "b.tech", "degree", "university",
        "college", "graduation"
    ]):
        improvements.append(
            "Add your educational qualifications."
        )


    # ROLE DETECTION

    if "react" in text or "html" in text or "css" in text:
        roles.append("Frontend Developer")

    if "python" in text or "django" in text or "flask" in text:
        roles.append("Python / Backend Developer")

    if "machine learning" in text:
        roles.append("Machine Learning Engineer")

    if "data analysis" in text or "tableau" in text:
        roles.append("Data Analyst")

    if "java" in text or "spring boot" in text:
        roles.append("Java Developer")

    if "node" in text:
        roles.append("Backend Developer")

    if not roles:
        roles.append("Software Developer")


    # BETTER RESUME BULLET POINTS

    better_bullets = [
        "Before: Worked on a project.",
        "After: Developed a project using relevant technologies and describe its measurable results.",
        "Before: Responsible for coding.",
        "After: Designed and implemented software modules using suitable programming technologies."
    ]


    # FINAL ATS SCORE

    ats_score = calculate_ats_score(resume_text)


    # PREPARE OUTPUT

    skills_str = (
        ", ".join(skills)
        if skills
        else "No technical skills detected."
    )

    missing_str = (
        ", ".join(missing_skills[:5])
        if missing_skills
        else "No missing skills from the checked list."
    )

    improvements_str = (
        "\n- ".join(improvements)
        if improvements
        else "No major missing sections detected by these basic checks."
    )

    roles_str = ", ".join(roles)


    result = f"""
📊 ATS Score: {ats_score}/100

🔍 Skills Detected:
- {skills_str}

⚠️ Skills Not Detected:
- {missing_str}

📈 Resume Improvements:
- {improvements_str}

✨ Better Resume Bullet Points:
- {better_bullets[0]}
- {better_bullets[1]}
- {better_bullets[2]}
- {better_bullets[3]}

💼 Recommended Career Roles:
- {roles_str}

Note: This is a basic keyword-based resume score,
not a professional ATS compatibility prediction.
"""

    return result.strip()
