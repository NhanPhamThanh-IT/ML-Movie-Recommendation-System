## Dataset guide (data/movies.csv)

This project uses a movie metadata file at `data/movies.csv` to build a content‑based recommender. The first few lines show typical fields:

Columns (abridged):

- index: Row identifier (not needed for modeling).
- id: TMDB movie id (string/integer).
- title, original_title: Movie titles.
- genres: Space‑separated genre string, e.g., "Action Adventure Fantasy".
- keywords: Space‑separated keywords, e.g., "space war society".
- overview: Plot summary.
- tagline: Short marketing tagline.
- cast: Top actors as a space‑separated list (pre‑flattened).
- director: Director name.
- homepage, release*date, status, runtime, budget, revenue, popularity, vote_average, vote_count, production*\*: Additional metadata (often unused for pure text‑based similarity but useful for filtering).

Note: Some columns (e.g., production_companies) contain JSON‑like strings; others are simplified into strings. We’ll mostly use text fields for TF‑IDF.

### Minimal modeling schema

For a content‑based recommender, we’ll derive a single text field per movie:

- text = concat_lower([
  title, tagline, overview, genres, keywords, cast, director
  ])

This makes a richer bag‑of‑words representation for TF‑IDF.

### Loading the dataset

```python
import pandas as pd

df = pd.read_csv("data/movies.csv")
df.head()
```

### Cleaning and preprocessing

Recommended steps:

- Fill missing text with empty strings to avoid NaN issues.
- Normalize to lowercase; strip whitespace.
- For columns that look like lists (e.g., cast), keep them as space‑separated tokens.
- Optionally remove punctuation and numbers from text fields.

Example:

```python
TEXT_COLS = [
	"title", "tagline", "overview", "genres", "keywords", "cast", "director"
]

for c in TEXT_COLS:
	if c in df.columns:
		df[c] = (
			df[c]
			.fillna("")
			.astype(str)
			.str.lower()
			.str.replace("\s+", " ", regex=True)
			.str.strip()
		)

df["text"] = df[TEXT_COLS].agg(" ".join, axis=1)
```

### Train/test hygiene

- If you plan to evaluate retrieval quality, split first (by movie id) before fitting the vectorizer.
- Keep a stable mapping from row index to `id`/`title` for back‑references.

### Sanity checks

- Duplicates: drop duplicate `id` or identical `text` rows.
- Empty text: remove or mark rows with `text == ""` after preprocessing.
- Non‑ASCII mishaps: ensure encoding is handled (UTF‑8 is default in pandas).

### Saving processed artifacts

- Persist the fitted TfidfVectorizer (pickle/joblib) and the TF‑IDF matrix (sparse CSR) for fast recommendations.
- Keep a small catalog DataFrame with at least `id`, `title`, and row index.

```python
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy import sparse
import joblib

vectorizer = TfidfVectorizer(
	stop_words="english",
	max_features=50000,
	ngram_range=(1, 2),
)
X = vectorizer.fit_transform(df["text"])  # CSR sparse matrix

joblib.dump(vectorizer, "artifacts/tfidf_vectorizer.joblib")
sparse.save_npz("artifacts/tfidf_matrix.npz", X)
df[["id", "title"]].to_csv("artifacts/catalog.csv", index=False)
```

### Extensions

- Use numeric features (runtime, year, vote_average) for filtering or hybrid scoring.
- Normalize dates to year and add as tokens (e.g., y2012) for temporal flavor.
- Extract named entities (actors/directors/companies) into distinct fields for faceted search.

### Related docs

- Feature extraction: [TF‑IDF](./TF-IDF.md)
- Similarity metric: [Cosine similarity](./cosine-similarity.md)
- Data wrangling: [pandas](./pandas.md)
