## TF‑IDF (Term Frequency – Inverse Document Frequency)

TF‑IDF converts text into numeric vectors that highlight terms distinctive to each document relative to the corpus.

Intuition:

- TF: how often a term appears in a document (normalized by document length).
- IDF: how rare a term is across the corpus (rarer → higher weight).
- TF‑IDF = TF × IDF gives high scores to terms that are frequent in a document but uncommon overall.

### Why use TF‑IDF here

- Movie overviews and metadata contain common words; TF‑IDF downweights them.
- Captures topical signals without requiring labels.
- Produces sparse vectors that scale to thousands of movies.

### scikit‑learn usage

```python
from sklearn.feature_extraction.text import TfidfVectorizer

corpus = df["text"].tolist()

vectorizer = TfidfVectorizer(
	stop_words="english",
	ngram_range=(1, 2),
	max_features=50000,
	min_df=2,
	sublinear_tf=True  # log‑scaled TF often helps
)
X = vectorizer.fit_transform(corpus)  # CSR sparse (n_docs × vocab)

# Inspect a feature or two
vocab = vectorizer.vocabulary_
print("term 'alien' -> index:", vocab.get("alien"))
```

### Making query vectors

Use the same fitted vectorizer to transform new text (e.g., a title or user query) into the same feature space.

```python
q = "space marines on a distant moon"
q_vec = vectorizer.transform([q])
```

### With cosine similarity

```python
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def search(query: str, top_k=10):
	q = vectorizer.transform([query])
	sims = cosine_similarity(q, X).ravel()
	top = np.argsort(-sims)[:top_k]
	return catalog.iloc[top].assign(score=sims[top])
```

### Parameter guidelines

- stop_words: remove frequent function words (e.g., English stop list).
- ngram_range: (1, 1) for unigrams; (1, 2) adds bigrams and often helps.
- max_features: cap vocabulary to control memory; 20–100k is common.
- min_df/max_df: prune very rare or very common terms.
- sublinear_tf: use log(1 + tf) to dampen heavy term counts.

### Pitfalls

- Fit leakage: fit the vectorizer only on training data when benchmarking.
- Locale/tokenization: default tokenization is simple; consider custom analyzers if needed.
- OOV terms: words unseen during fit are ignored at transform time.

### Related topics

- Similarity metric: [Cosine similarity](./cosine-similarity.md)
- Library glue: [scikit‑learn](./scikit-learn.md), [pandas](./pandas.md)
