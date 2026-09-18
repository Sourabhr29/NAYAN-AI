from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="NAYAN AI")

app.mount("/app", StaticFiles(directory="frontend", html=True), name="frontend")

@app.get("/")
def home():
    return {
        "name": "NAYAN AI",
        "status": "online",
        "message": "NAYAN AI backend is running"
    }

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/ask")
def ask(question: str):
    return {"answer": f"NAYAN AI received your question: {question}"}
