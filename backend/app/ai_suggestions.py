# ✅ ATS SCORE FUNCTION
def calculate_ats_score(resume_text):
    text = resume_text.lower()

    score = 0
    total = 5   # total checks

    # Check 1: Skills
    if any(skill in text for skill in ["python", "java", "react", "sql"]):
        score += 1

    # Check 2: Projects
    if "project" in text:
        score += 1

    # Check 3: Experience
    if "internship" in text or "experience" in text:
        score += 1

    # Check 4: Achievements
    if any(word in text for word in ["improved", "increased", "%", "optimized"]):
        score += 1

    # Check 5: Tools
    if any(word in text for word in ["git", "github", "docker", "aws"]):
        score += 1

    final_score = int((score / total) * 100)
    return final_score


# ✅ MAIN AI FUNCTION
def get_suggestions(resume_text):
    text = resume_text.lower()

    skills = []
    missing_skills = []
    improvements = []
    roles = []

    skill_list = [
        "python", "java", "c++", "react", "node", "sql",
        "html", "css", "javascript", "machine learning",
        "data analysis", "spring boot", "django", "flask"
    ]

    for skill in skill_list:
        if skill in text:
            skills.append(skill)
        else:
            missing_skills.append(skill)

    if "project" not in text:
        improvements.append("Add 2-3 strong projects with clear descriptions and outcomes")

    if "internship" not in text:
        improvements.append("Include internship or practical experience to strengthen credibility")

    if "achiev" not in text:
        improvements.append("Mention achievements with measurable results (e.g., improved performance by 20%)")

    if "team" not in text:
        improvements.append("Highlight teamwork or collaboration experience")

    # Role detection
    if "react" in text or "html" in text:
        roles.append("Frontend Developer")

    if "python" in text or "django" in text:
        roles.append("Backend Developer")

    if "machine learning" in text or "data" in text:
        roles.append("Data Scientist / Data Analyst")

    if "java" in text:
        roles.append("Java Developer")

    if not roles:
        roles.append("Software Developer")

    better_bullets = [
        "Before: Worked on a project → After: Developed a full-stack project improving efficiency by 30%",
        "Before: Responsible for coding → After: Designed scalable modules using best practices"
    ]

    # ✅ CALL ATS SCORE HERE
    ats_score = calculate_ats_score(resume_text)

    # Prepare strings
    skills_str = ", ".join(skills) if skills else "No strong technical skills detected"
    missing_str = ", ".join(missing_skills[:5])
    improvements_str = "\n- ".join(improvements) if improvements else "Profile looks good, minor refinements needed"
    roles_str = ", ".join(roles)

    # Final result
    result = f"""
📊 ATS Score: {ats_score}/100

🔍 Skills Detected:
- {skills_str}

⚠️ Missing Skills:
- {missing_str}

📈 Improvements:
- {improvements_str}

✨ Better Resume Bullet Points:
- {better_bullets[0]}
- {better_bullets[1]}

💼 Recommended Roles:
- {roles_str}
"""

    return result.strip()