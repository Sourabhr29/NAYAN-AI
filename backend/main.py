from fastapi import FastAPI

app = FastAPI(title="NAYAN AI")

@app.get("/")
def home():
    return {
        "name": "NAYAN AI",
        "status": "online",
        "message": "NAYAN AI backend is running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
}