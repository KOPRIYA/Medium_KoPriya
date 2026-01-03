import time
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import vector_search

vectors = np.random.rand(2000, 128)
query = np.random.rand(1, 128)

# Python-only
start = time.time()
cosine_similarity(vectors, query)
print("Python latency:", time.time() - start)

# C++ backed
start = time.time()
vector_search.find_most_similar(vectors.tolist(), query[0].tolist())
print("C++ backed latency:", time.time() - start)