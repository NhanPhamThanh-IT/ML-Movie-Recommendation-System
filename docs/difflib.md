## Fuzzy matching with difflib

`difflib` is a Python standard library for comparing sequences. For a recommender, it’s handy to map a user’s noisy input (e.g., misspelled movie title) to the closest known title.

### Core functions

- SequenceMatcher: computes similarity ratio between two strings.
- get_close_matches: returns the best matches for a word from a list.

### Quick start

```python
from difflib import get_close_matches, SequenceMatcher

word = "avatr"  # user typed
candidates = ["Avatar", "Avengers", "Arrival", "Aviator"]

print(get_close_matches(word, candidates, n=3, cutoff=0.6))
# ['Avatar', 'Aviator']

print(SequenceMatcher(None, "pirats", "pirates").ratio())
# ~0.86
```

### Integrating with the catalog

```python
import pandas as pd
from difflib import get_close_matches

catalog = pd.read_csv("artifacts/catalog.csv")  # has columns: id, title
titles = catalog["title"].astype(str).tolist()

def resolve_title(query: str, n=5, cutoff=0.6):
	matches = get_close_matches(query, titles, n=n, cutoff=cutoff)
	return catalog[catalog.title.isin(matches)]

print(resolve_title("pirats of the caribean"))
```

### Tips

- Lowercase both query and titles for consistent matching.
- Tune `cutoff` (0–1) to control strictness; combine with exact startswith/contains checks.
- For large catalogs, consider faster libraries (rapidfuzz/fuzzywuzzy) or use token set ratios.

### Caveats

- `difflib` is O(n) over candidates; may feel slow for hundreds of thousands of titles.
- String similarity may conflate distinct titles with similar spellings.

### See also

- Data handling: [pandas](./pandas.md)
- Vector search alternative: [TF‑IDF](./TF-IDF.md) + [Cosine similarity](./cosine-similarity.md)
