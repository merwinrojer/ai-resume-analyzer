import re

SKILLS_DB = [
    "python",
    "fastapi",
    "sqlalchemy",
    "postgresql",
    "docker",
    "aws",
    "git",
    "github",
    "jwt",
    "rest api"
]

def extract_skills(text: str):
    text = text.lower()
    found_skills = []

    for skill in SKILLS_DB:
        if re.search(rf"\b{skill}\b", text):
            found_skills.append(skill)

    return list(set(found_skills))

def analyze_resume_score(text: str):

    skills_found = extract_skills(text)

    missing_skills = []

    for skill in SKILLS_DB:
        if skill not in skills_found:
            missing_skills.append(skill)

    score = int(
        (len(skills_found) / len(SKILLS_DB)) * 100
    )

    return {
        "score": score,
        "skills_found": skills_found,
        "missing_skills": missing_skills
    }