from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from datetime import datetime

from app.ai_client import ask_ai

app = FastAPI()

# Allow your frontend (Live Server) to call the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AskRequest(BaseModel):
    question: str
    correctness: int  # 1-5
    clarity: int      # 1-5
    hallucination: bool
    notes: str = ""

class EvaluationRecord(BaseModel):
    id: int
    created_at: str
    question: str
    answer: str
    correctness: int
    clarity: int
    hallucination: bool
    notes: str

# In-memory storage for Day 3
EVALS: List[EvaluationRecord] = []
NEXT_ID = 1

@app.post("/ask")
def ask_and_evaluate(payload: AskRequest):
    global NEXT_ID

    answer = ask_ai(payload.question)

    record = EvaluationRecord(
        id=NEXT_ID,
        created_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        question=payload.question,
        answer=answer,
        correctness=payload.correctness,
        clarity=payload.clarity,
        hallucination=payload.hallucination,
        notes=payload.notes,
    )
    NEXT_ID += 1
    EVALS.insert(0, record)  # newest first

    return record

@app.get("/evaluations")
def get_evaluations():
    return EVALS
