import numpy as np
import vector_search

vectors = np.random.rand(1000, 128).tolist()
query = np.random.rand(128).tolist()

idx = vector_search.find_most_similar(vectors, query)
print("Most similar vector index:", idx)