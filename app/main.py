# Import the FastAPI class from the fastapi package.
# FastAPI is the framework I use to build web APIs in Python.
# Import BaseModel from Pydantic.
# BaseModel is used to define the structure of data 
# that the API expects to receive from users.
# FastAPI uses this to validate incoming request data automatically.
from fastapi import FastAPI
from pydantic import BaseModel
from app.ai_client import ask_ai 
from fastapi.middleware.cors import CORSMiddleware

# Create an instance of the FastAPI application.
# This object represents my web server.
# All API routses (endpoints) will be attached to this app.

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow the frontend to call the backend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# This class defines the structure of data that the API expects
# to receive from the user when calling the /ask endpoint.
# FastAPI uses this to validate incoming request data automatically.
class QuestionRequest(BaseModel):
    question: str



# Create an instance of the FastAPI application.
# This object represents my web server.
# All API routses (endpoints) will be attached to this app.


# The @app.get("/") decorator defines an API endpoint.
# when user sends a GET request
# to the root URL ("/")
# run the function below and return its result.
# Example: 
# http://127.0.0.1:8000/
@app.get("/")
def root():
    # This function runs when someone visitsthe root URL.
    # FastAPI automatically converts this Python dictionary
    # into JSON and sends it back to the browser or API client.
    return {"message": "AI Response Evaluator Running"}


# This endpoint receives a question from the user.
# The request body must watch the QuestionRequest schema above.
#
# FastAPI automatically:
# - reads the incoming JSON
# - validates it using QuestionRequest
# - converts it into Python object
#
# Later this question will be sent to an AI model.
@app.post("/ask")
def ask_question(request: QuestionRequest):
    # For now, we just return the received question.
    # This confirms that the API is correctly receiving user input.
    return {
        "received_question": request.question,
        "answer": ask_ai(request.question)
    }

