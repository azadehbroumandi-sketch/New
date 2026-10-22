"""Square-root operations."""

import math
import numbers


def sqrt(value):
    """Return the non-negative square root of a real number.

    Args:
        value: A real number other than ``bool``.

    Raises:
        TypeError: If *value* is not a real number.
        ValueError: If *value* is negative.
    """
    if isinstance(value, bool) or not isinstance(value, numbers.Real):
        raise TypeError("sqrt() requires a real number")
    if value < 0:
        raise ValueError("sqrt() is undefined for negative numbers")
    if value == 0:
        return 0.0
    return math.sqrt(value)
