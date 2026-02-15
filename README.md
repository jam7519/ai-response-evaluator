# AI Response Evaluator

AI Response Evaluator is a simple full-stack AI application built with FastAPI and a lightweight HTML frontend.

The application allows users to submit questions to an AI model and receive responses through a clean web interface.

---

## Features

- FastAPI backend
- AI integration using OpenAI API
- Simple modern frontend
- Secure API key handling using environment variables
- Swagger documentation
- Local development setup

---

## Architecture

Frontend (HTML / JS)
        ↓
FastAPI Backend (Port 8000)
        ↓
OpenAI API

---

## Setup Instructions

git clone https://github.com/jam7519/ai-response-evaluator.git

cd ai-response-evaluator


### 2. Create virtual environment


python -m venv venv
venv\Scripts\activate


### 3. Install dependencies

pip install fastapi uvicorn openai python-dotenv


### 4. Create .env file

Create a file named `.env`:

OPENAI_API_KEY=your_api_key_here


### 5. Run backend

python -m uvicorn app.main:app --reload


Open:

http://127.0.0.1:8000/docs


### 6. Run frontend

Open:

app/frontend/index.html


---

## Future Improvements

- Response history
- AI evaluation scoring
- UI improvements
- Cloud deployment


### 1. Clone repository

