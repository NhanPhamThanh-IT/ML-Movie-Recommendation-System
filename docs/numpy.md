## NumPy essentials for this project

NumPy provides fast, vectorized computation on n‑dimensional arrays. In this project, you’ll use NumPy to:

- Compute norms and dot products (for cosine similarity if doing it manually).
- Manipulate indices and scores from similarity matrices.

### Core concepts

- ndarray: typed, homogeneous array.
- Vectorized ops: `a + b`, `a * b`, `a @ b` operate elementwise or as matrix multiplication.
- Broadcasting: operations between arrays of different shapes when compatible.

### Useful snippets

```python
import numpy as np

a = np.array([1.0, 2.0, 0.0, 3.0])
b = np.array([0.0, 1.0, 0.0, 1.0])

dot = a @ b
norms = np.linalg.norm(a) * np.linalg.norm(b)
cos = dot / norms if norms else 0.0

# Top‑k indices from scores
scores = np.array([0.1, 0.9, 0.2, 0.7])
topk = np.argsort(-scores)[:3]  # [1, 3, 2]
```

### Sparse vs dense

TF‑IDF matrices are typically sparse. Prefer SciPy sparse matrices for memory and speed:

```python
from scipy import sparse

# Create a 3x4 sparse CSR matrix
row = np.array([0, 0, 1])
col = np.array([1, 3, 2])
data = np.array([0.5, 0.8, 1.0])
X = sparse.csr_matrix((data, (row, col)), shape=(3, 4))
```

### Tips

- Avoid converting large sparse matrices to dense arrays.
- Use `astype(np.float32)` to reduce memory when precision is sufficient.
- Check shapes and dtypes (`a.shape`, `a.dtype`) to preempt broadcasting mistakes.

### See also

- DataFrames interop: [pandas](./pandas.md)
- Modeling: [scikit‑learn](./scikit-learn.md)
