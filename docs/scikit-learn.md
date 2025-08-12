## Scikit‑learn in this project

scikit‑learn provides the building blocks to vectorize text and compute similarities at scale.

### TF‑IDF vectorization

```python
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(
	stop_words="english",
	max_features=50000,
	ngram_range=(1, 2),
	min_df=2
)
X = vectorizer.fit_transform(df["text"])  # CSR sparse matrix
```

### Cosine similarity

```python
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def top_k_similar(X, idx, k=10):
	sims = cosine_similarity(X[idx], X).ravel()
	sims[idx] = -1
	top = np.argsort(-sims)[:k]
	return top, sims[top]
```

### Dimensionality reduction (optional)

Truncated SVD (a.k.a. latent semantic analysis) can denoise and speed up similarity.

```python
from sklearn.decomposition import TruncatedSVD
from sklearn.preprocessing import Normalizer
from sklearn.pipeline import make_pipeline

svd = TruncatedSVD(n_components=300, random_state=42)
normalizer = Normalizer(copy=False)
lsa = make_pipeline(svd, normalizer)

X_lsa = lsa.fit_transform(X)  # dense matrix (n_docs × n_components)
```

If memory is tight, keep the original sparse TF‑IDF and skip SVD.

### Pipelines and persistence

```python
import joblib

joblib.dump(vectorizer, "artifacts/tfidf_vectorizer.joblib")
joblib.dump(svd, "artifacts/svd.joblib")  # if used
```

### Parameter tips

- stop_words: use "english" to remove common terms.
- ngram_range: (1, 2) often boosts accuracy via short phrases.
- max_features: cap vocabulary to control memory/latency.
- min_df or max_df: prune extremely rare or overly common terms.

### Evaluating changes

- Compare nearest neighbors for a few anchor titles before/after a change.
- Track latency for a single query and for batch queries.

### See also

- Text features: [TF‑IDF](./TF-IDF.md)
- Metric: [Cosine similarity](./cosine-similarity.md)
