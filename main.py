from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import engine, get_db
from models import Base, User,Resume,Analysis
from schemas import UserCreate, UserLogin, ResumeCreate
from utils import hash_password, verify_password
from ai_utils import extract_skills,analyze_resume_score

from auth import create_access_token,verify_token,get_current_user_id
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def home():
    return {"message": "AI Resume Analyzer API"}


@app.post("/users")
def create_user(user: UserCreate, db: Session = Depends(get_db)):

    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if existing_user:
        return {"message": "Email already registered"}

    new_user = User(
        name=user.name,
        email=user.email,
        password=hash_password(user.password)
    )

    db.add(new_user)
    db.commit()

    return {"message": "User created successfully"}


@app.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):

    db_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if not db_user:
        return {"message": "User not found"}

    if not verify_password(
        user.password,
        db_user.password
    ):
        return {"message": "Invalid password"}

    token = create_access_token(
    {"user_id": db_user.id}
)
    return {
    "access_token": token,
    "token_type": "bearer"
}

@app.post("/upload-resume")
def upload_resume(
    resume: ResumeCreate,
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):

    token = credentials.credentials

    user_id = get_current_user_id(token)

    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        return {"message": "User not found"}

    new_resume = Resume(
        filename=resume.filename,
        resume_text=resume.resume_text,
        user_id=user_id
    )

    db.add(new_resume)
    db.commit()

    return {"message": "Resume uploaded successfully"}

@app.post("/analyze-resume/{resume_id}")
def analyze_resume(
    resume_id: int,
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):

    token = credentials.credentials

    user_id = get_current_user_id(token)

    resume = db.query(Resume).filter(
        Resume.id == resume_id,
        Resume.user_id == user_id
    ).first()

    if not resume:
        return {"message": "Resume not found"}
    result = analyze_resume_score(resume.resume_text)
    analysis = Analysis(
    skills_found=", ".join(result["skills_found"]),
    resume_id=resume.id
)

    db.add(analysis)
    db.commit()

    skills = extract_skills(resume.resume_text)

    return {
    "resume_id": resume_id,
    "filename": resume.filename,
    "score": result["score"],
    "skills_found": result["skills_found"],
    "missing_skills": result["missing_skills"]
}

# @app.post("/classify-resume/{resume_id}")
# def classify_resume_endpoint(
#     resume_id: int,
#     db: Session = Depends(get_db)
# ):

#     resume = db.query(Resume).filter(
#         Resume.id == resume_id
#     ).first()

#     if not resume:
#         return {"message": "Resume not found"}

#     return classify_resume(
#         resume.resume_text
#     )

@app.get("/test-token")
def test_token():

    token = create_access_token(
        {"user_id": 1}
    )

    return {"token": token}


@app.get("/protected")
def protected_route(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):

    token = credentials.credentials

    payload = verify_token(token)

    return {
        "message": "Access granted",
        "user": payload
    }

@app.get("/my-resumes")
def get_my_resumes(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):

    token = credentials.credentials

    user_id = get_current_user_id(token)

    resumes = db.query(Resume).filter(
        Resume.user_id == user_id
    ).all()

    return resumes

@app.get("/my-analyses")
def get_my_analyses(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):

    token = credentials.credentials

    user_id = get_current_user_id(token)

    analyses = (
        db.query(Analysis)
        .join(Resume)
        .filter(Resume.user_id == user_id)
        .all()
    )

    return analyses