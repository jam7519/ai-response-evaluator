from typing import List, Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.ai_client import ask_ai  # uses your ai_client.py

app = FastAPI()

# Allow your frontend (Live Server) to call the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500",
        "http://127.0.0.1:5173",  # optional (vite)
        "http://localhost:5173",  # optional (vite)
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory history (we'll replace with SQLite later)
EVAL_HISTORY: List[dict] = []


class EvalRequest(BaseModel):
    question: str
    correctness: int
    clarity: int
    hallucination: bool
    notes: Optional[str] = ""


class EvalRecord(BaseModel):
    question: str
    answer: str
    correctness: int
    clarity: int
    hallucination: bool
    notes: str


@app.get("/health")
def health():
    return {"ok": True}


@app.post("/evaluate", response_model=EvalRecord)
def evaluate(req: EvalRequest):
    answer = ask_ai(req.question)

    record = {
        "question": req.question,
        "answer": answer,
        "correctness": int(req.correctness),
        "clarity": int(req.clarity),
        "hallucination": bool(req.hallucination),
        "notes": (req.notes or "").strip(),
    }

    # newest first
    EVAL_HISTORY.insert(0, record)
    return record


@app.get("/history")
def history():
    return EVAL_HISTORY
