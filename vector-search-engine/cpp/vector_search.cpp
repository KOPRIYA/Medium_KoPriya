#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <vector>
#include <cmath>
#include <limits>

namespace py = pybind11;

double cosine_similarity(const std::vector<double>& a,
                          const std::vector<double>& b) {
    double dot = 0.0, na = 0.0, nb = 0.0;
    for (size_t i = 0; i < a.size(); i++) {
        dot += a[i] * b[i];
        na += a[i] * a[i];
        nb += b[i] * b[i];
    }
    return dot / (std::sqrt(na) * std::sqrt(nb));
}

int find_most_similar(
    const std::vector<std::vector<double>>& vectors,
    const std::vector<double>& query
) {
    double best_score = -std::numeric_limits<double>::infinity();
    int best_index = -1;

    for (size_t i = 0; i < vectors.size(); i++) {
        double score = cosine_similarity(vectors[i], query);
        if (score > best_score) {
            best_score = score;
            best_index = i;
        }
    }
    return best_index;
}

PYBIND11_MODULE(vector_search, m) {
    m.def("find_most_similar", &find_most_similar,
          "Find most similar vector index");
}