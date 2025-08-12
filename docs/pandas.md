## Pandas for data wrangling

pandas is the go‑to library for loading, cleaning, and transforming tabular data.

### Load data

```python
import pandas as pd

df = pd.read_csv("data/movies.csv")
df.info()
df.head()
```

### Select and clean text columns

```python
TEXT_COLS = ["title", "tagline", "overview", "genres", "keywords", "cast", "director"]

for c in TEXT_COLS:
	if c in df.columns:
		df[c] = (
			df[c].fillna("").astype(str).str.lower().str.replace("\s+", " ", regex=True).str.strip()
		)

df["text"] = df[TEXT_COLS].agg(" ".join, axis=1)
```

### Filtering and sampling

```python
# Drop rows without usable text
df = df[df["text"].str.len() > 0].copy()

# Keep necessary columns for the catalog
catalog = df[["id", "title"]].copy()

# Quick sample for prototyping
small = df.sample(2000, random_state=42) if len(df) > 2000 else df
```

### Merging and joining

- If you split artifacts (e.g., vector rows) from the catalog, keep a stable index or add a `row_idx` column.
- Use `merge` on `id` to reattach metadata to recommendations.

```python
recs = pd.DataFrame({"id": [19995, 49026], "score": [0.78, 0.74]})
out = recs.merge(catalog, on="id", how="left")
```

### Exporting

```python
catalog.to_csv("artifacts/catalog.csv", index=False)
```

### See also

- Numeric array ops: [NumPy](./numpy.md)
- Feature extraction: [TF‑IDF](./TF-IDF.md)
