"""A small command-line calculator and reusable arithmetic functions."""

from __future__ import annotations

import argparse
from numbers import Real
from typing import Union

Number = Union[int, float]



def _validate_numbers(left: Number, right: Number) -> None:
    """Validate that both operands are real numbers, excluding booleans."""
    if isinstance(left, bool) or isinstance(right, bool):
        raise TypeError("operands must be real numbers")
    if not isinstance(left, Real) or not isinstance(right, Real):
        raise TypeError("operands must be real numbers")



def add(left: Number, right: Number) -> Number:
    """Return the sum of two real numbers."""
    _validate_numbers(left, right)
    return left + right



def subtract(left: Number, right: Number) -> Number:
    """Return the difference between two real numbers."""
    _validate_numbers(left, right)
    return left - right



def multiply(left: Number, right: Number) -> Number:
    """Return the product of two real numbers."""
    _validate_numbers(left, right)
    return left * right



def divide(left: Number, right: Number) -> float:
    """Return the quotient of two real numbers.

    Raises:
        ZeroDivisionError: if ``right`` is zero.
    """
    _validate_numbers(left, right)
    if right == 0:
        raise ZeroDivisionError("cannot divide by zero")
    return left / right


_OPERATIONS = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculate(left: Number, operator: str, right: Number) -> Number:
    """Apply an arithmetic operator to two validated operands."""
    if not isinstance(operator, str) or operator not in _OPERATIONS:
        raise ValueError(f"unsupported operator: {operator!r}")
    return _OPERATIONS[operator](left, right)



def main() -> None:
    """Run the calculator command-line interface."""
    parser = argparse.ArgumentParser(description="Perform a basic calculation.")
    parser.add_argument("left", type=float, nargs="?", help="first number")
    parser.add_argument("operator", nargs="?", choices=sorted(_OPERATIONS), help="+ - * /")
    parser.add_argument("right", type=float, nargs="?", help="second number")
    args = parser.parse_args()

    if args.left is None or args.operator is None or args.right is None:
        parser.error("provide a number, an operator, and another number")

    try:
        result = calculate(args.left, args.operator, args.right)
    except ZeroDivisionError as error:
        parser.error(str(error))
    print(result)


if __name__ == "__main__":
    main()
