# AI Resume Analyzer

## Overview

AI Resume Analyzer is a backend application built with FastAPI and PostgreSQL that helps users upload resumes, extract skills, analyze technical profiles, and track resume evaluations.

The project demonstrates authentication, database design, file processing, and AI-powered resume analysis concepts commonly used in modern recruitment and HR technology platforms.

---

## Features

### Authentication

* User Registration
* Secure Login
* JWT Token Authentication
* Protected Endpoints

### Resume Management

* Upload Resumes
* Store Resume Data
* Retrieve Resume History

### Resume Analysis

* Extract Technical Skills
* Analyze Resume Content
* Store Analysis Results
* View Previous Analyses

### Database Integration

* PostgreSQL Database
* SQLAlchemy ORM
* Relational Data Modeling

---

## Tech Stack

### Backend

* Python
* FastAPI

### Database

* PostgreSQL
* SQLAlchemy ORM

### Security

* JWT Authentication
* Passlib (bcrypt)

### AI & Processing

* Resume Skill Extraction
* Resume Analysis Engine

---

## Project Structure

```text
ai-resume-analyzer
│
├── main.py
├── models.py
├── schemas.py
├── crud.py
├── auth.py
├── database.py
└── requirements.txt
```

---

## API Endpoints

### Authentication

```http
POST /users
POST /login
```

### Resume Management

```http
POST /upload-resume
GET /my-resumes
```

### Resume Analysis

```http
POST /analyze-resume/{resume_id}
GET /my-analyses
```

---

## How to Run Locally

### Clone Repository

```bash
git clone https://github.com/merwinrojer/ai-resume-analyzer.git
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Server

```bash
uvicorn main:app --reload
```

### Open Swagger Documentation

```text
http://127.0.0.1:8000/docs
```

---

## Concepts Demonstrated

* REST API Development
* Authentication & Authorization
* PostgreSQL Database Design
* SQLAlchemy ORM
* Resume Processing
* Backend Architecture
* AI-Assisted Analysis

---

## Future Improvements

* PDF Resume Upload Support
* Job Description Matching
* Resume Scoring System
* Skill Gap Analysis
* AI-Powered Suggestions
* Docker Deployment

---
## live demo
https://ai-resume-analyzer-3pns.onrender.com/docs

## Author

Merwin Rojer C

Backend Developer | Python | FastAPI | PostgreSQL | AI Applications
