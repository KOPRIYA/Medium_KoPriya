from fastapi import FastAPI
from app.rag.pipeline import RAGPipeline

app = FastAPI()
pipeline = RAGPipeline()

@app.post("/recommend")
def recommend(payload: dict):
    return {
        "recommendation": pipeline.run(
            payload["requirements"],
            payload["kpis"]
        )
    }