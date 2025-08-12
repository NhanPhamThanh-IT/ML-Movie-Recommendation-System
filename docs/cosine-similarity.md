## Cosine similarity

Cosine similarity measures how similar two vectors are by the cosine of the angle between them. It is scale-invariant (only the direction matters), which makes it ideal for comparing text vectors like TF‑IDF where magnitude can be influenced by document length.

- Range: [-1, 1] for real-valued vectors, [0, 1] for non‑negative vectors (e.g., TF‑IDF).
- 1 = identical direction, 0 = orthogonal/unrelated, -1 = opposite.

Mathematically, for vectors a and b:

cos_sim(a, b) = (a · b) / (||a|| · ||b||)

### Why it’s great for text

- Normalizes away length differences between documents.
- Emphasizes overlap of informative features (words/terms) after weighting (e.g., TF‑IDF).
- Works well with sparse, high‑dimensional vectors.

### In a movie recommender

- Represent each movie by a TF‑IDF vector over fields like overview, keywords, tagline, and genres.
- Similar movies have higher cosine similarity to a given movie/user query.

### Quick examples

Compute cosine similarity with NumPy:

```python
import numpy as np

def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
	denom = (np.linalg.norm(a) * np.linalg.norm(b))
	if denom == 0:
		return 0.0
	return float(np.dot(a, b) / denom)

a = np.array([1, 2, 0, 3])
b = np.array([0, 1, 0, 1])
print(cosine_similarity(a, b))  # ~0.866
```

With scikit‑learn for many pairs efficiently:

```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

docs = [
	"a space marine protects an alien civilization on a distant moon",
	"pirates sail to the edge of the world",
]

tfidf = TfidfVectorizer(stop_words="english")
X = tfidf.fit_transform(docs)   # sparse matrix (n_docs × n_terms)

S = cosine_similarity(X)        # (n_docs × n_docs)
print(S)
```

### Practical tips

- Use cosine_similarity(X, Y) on sparse matrices to avoid densifying.
- Precompute norms once if you’ll do many query comparisons.
- Consider dimensionality reduction (e.g., TruncatedSVD) for speed on very large vocabularies.
- Remove boilerplate terms with stop words and/or min_df to reduce noisy overlaps.

### Common pitfalls

- Zero vectors: if a document becomes empty after preprocessing, its norm is 0. Guard against divide-by-zero and treat similarity as 0.
- Feature leakage: ensure validation splits happen before fitting vectorizers.
- Sparsity explosion: control vocabulary with max_features, min_df, or n‑grams.

### See also

- TF‑IDF basics: [TF‑IDF](./TF-IDF.md)
- End‑to‑end pipeline: [scikit‑learn](./scikit-learn.md)
