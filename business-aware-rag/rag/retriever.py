import faiss
import numpy as np
import json

class Retriever:
    def __init__(self, embeddings, metadata):
        dim = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dim)
        self.index.add(embeddings)
        self.metadata = metadata

    def search(self, query_embedding, k=3):
        D, I = self.index.search(np.array([query_embedding]), k)
        return [self.metadata[i] for i in I[0]]