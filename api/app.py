from fastapi import FastAPI
from main import run_agent

app = FastAPI()

@app.get("/ask")
def ask(question: str):
    return {
        "answer": run_agent(question)
    }