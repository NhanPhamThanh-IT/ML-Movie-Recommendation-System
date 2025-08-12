## Machine learning for recommendations

Recommender systems suggest relevant items to users. Two common paradigms:

- Collaborative filtering: learns from user–item interactions (ratings, clicks). Needs many users and interactions; can generalize well but cold‑start is hard.
- Content‑based filtering: uses item features (text, metadata) to find similar items. Works even with few users; ideal when you have rich item content.

This project implements a content‑based recommender using movie metadata (overview, genres, keywords, cast, director) and text vectors (TF‑IDF) with cosine similarity.

### Pipeline

1. Ingest and clean the dataset.
2. Build a unified textual representation per movie.
3. Vectorize with TF‑IDF.
4. Compute similarities; return top‑k most similar movies.

### Why TF‑IDF + cosine

- TF‑IDF downweights ubiquitous words and elevates distinctive terms.
- Cosine similarity is length‑invariant and works well on sparse vectors.

### Possible upgrades

- N‑grams (unigrams + bigrams) to capture short phrases.
- Dimensionality reduction (Truncated SVD) for faster search and noise reduction.
- Hybrid models: blend TF‑IDF similarity with numeric features (year, rating) or lightweight collaborative signals.
- ANN search (FAISS, NMSLIB) for sub‑linear retrieval at scale.

### Evaluation

Without user labels, use intrinsic checks:

- Spot‑check nearest neighbors for well‑known titles.
- Diversity/novelty checks: avoid redundant results by post‑filtering.
- If you have partial ground truth (e.g., franchise lists), compute precision@k within those sets.

### Risks and mitigations

- Popularity bias: if you include popularity or votes, it can drown out niche items; use it only for tie‑breaking.
- Data noise: malformed JSON‑like fields; sanitize robustly.
- Cold/empty items: drop or enrich items with very short texts.

### References

- See [TF‑IDF](./TF-IDF.md), [Cosine similarity](./cosine-similarity.md), and [scikit‑learn](./scikit-learn.md) for implementation details.
