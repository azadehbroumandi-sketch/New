# Square-root operation

The public API is `sqrt.sqrt(value)`. It accepts real numeric values other than
`bool` and returns the non-negative square root as a `float`.

- Negative values raise `ValueError`.
- Non-real values and booleans raise `TypeError`.
- Zero returns positive `0.0`; infinity and NaN follow the behavior of `math.sqrt`.
