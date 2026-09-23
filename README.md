# extended-euclidean-algorithm

`extended_gcd(a, b)` returns `(gcd, x, y)` such that `a*x + b*y = gcd` for integers `a` and `b`.

```python
from extended_euclidean_algorithm import extended_gcd

gcd, x, y = extended_gcd(240, 46)
print(gcd, x, y)          # 2 -9 47
print(240*x + 46*y)       # 2
```

The function is useful for computing modular inverses and finding particular solutions to linear Diophantine equations.

## Why this exists

Most implementations of the extended Euclidean algorithm are recursive and can hit Python's recursion limit for large inputs. This version uses an iterative loop, which avoids that problem entirely. It also normalizes the returned gcd to be non-negative, matching the convention of Python's `math.gcd`.

## Edge case

Calling `extended_gcd(0, 0)` returns `(0, 0, 0)`. The gcd of two zeros is conventionally defined as zero, and any pair of coefficients satisfies the identity, so returning zeros keeps the result deterministic and simple to reason about.
