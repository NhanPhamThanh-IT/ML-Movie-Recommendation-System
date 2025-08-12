## Working with Jupyter Notebooks

This project includes a `notebook.ipynb` to explore the dataset and build the recommender. Here’s how to use notebooks effectively in this repo.

### Setup

1. Create and activate a Python environment (3.9+ recommended).
2. Install packages: pandas, numpy, scikit‑learn, scipy, joblib, jupyter.
3. Launch Jupyter and open `notebook.ipynb`.

### Notebook structure suggestions

- Data loading: inspect `data/movies.csv`, select columns, clean text.
- Feature extraction: build TF‑IDF, persist vectorizer/matrix.
- Similarity search: cosine similarity to get recommendations.
- UI utilities: helper functions for fuzzy title lookup and pretty printing.

### Reproducibility tips

- Set a cell at the top to fix random seeds (numpy, Python, scikit‑learn where applicable).
- Avoid hard‑coding paths; use relative paths like `data/movies.csv`.
- Keep heavy work (fitting TF‑IDF) in functions and cache outputs (e.g., .npz, .joblib).

### Performance

- Prefer sparse matrices and vectorized operations.
- Use incremental development: work on a small sample first (`df.sample(5000)`) before scaling up.
- For many queries, precompute norms and use efficient batch functions (`cosine_similarity`).

### Debugging

- Inspect shapes and dtypes often (`X.shape`, `X.nnz`).
- Print a couple of tokenized examples to verify preprocessing.
- Validate that no empty `text` rows remain after cleaning.

### Exporting results

- Save artifacts to an `artifacts/` folder: vectorizer, TF‑IDF matrix, and catalog.
- Save sample recommendations as CSV or JSON for quick tests.

### Handy snippets

Create a recommend function inside the notebook:

```python
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def recommend_by_title(title: str, catalog, X, vectorizer, top_k=10):
	# Find index of exact title
	matches = catalog.index[catalog.title.str.lower() == title.lower()].tolist()
	if not matches:
		return []
	idx = matches[0]
	# Compute similarity row-wise
	sims = cosine_similarity(X[idx], X).ravel()
	# Exclude itself
	sims[idx] = -1
	top = np.argsort(-sims)[:top_k]
	return catalog.iloc[top].assign(score=sims[top])
```

### Related docs

- Data: [Dataset](./dataset.md)
- Vectors: [TF‑IDF](./TF-IDF.md)
- Metric: [Cosine similarity](./cosine-similarity.md)
