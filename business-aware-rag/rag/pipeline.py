from .embedder import Embedder
from .retriever import Retriever
from .prompt import build_prompt
from .generator import generate
import json

class RAGPipeline:
    def __init__(self):
        with open("app/data/past_solutions.json") as f:
            self.data = json.load(f)

        self.embedder = Embedder()
        self.embeddings = self.embedder.embed(
            [d["description"] for d in self.data]
        )
        self.retriever = Retriever(self.embeddings, self.data)

    def run(self, requirements, kpis):
        query_embedding = self.embedder.embed([requirements])[0]
        contexts = self.retriever.search(query_embedding)
        prompt = build_prompt(requirements, kpis, contexts)
        return generate(prompt)