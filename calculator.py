"""A small command-line calculator and reusable arithmetic functions."""

from __future__ import annotations

import argparse
import math
from numbers import Real
from typing import Union

Number = Union[int, float]



def _validate_numbers(left: Number, right: Number) -> None:
    """Validate that both operands are real numbers, excluding booleans."""
    if isinstance(left, bool) or isinstance(right, bool):
        raise TypeError("operands must be real numbers")
    if not isinstance(left, Real) or not isinstance(right, Real):
        raise TypeError("operands must be real numbers")



def _validate_number(value: Number) -> None:
    """Validate that a value is a real number, excluding booleans."""
    if isinstance(value, bool) or not isinstance(value, Real):
        raise TypeError("operand must be a real number")



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



def sqrt(value: Number) -> float:
    """Return the non-negative square root of a real number.

    Raises:
        ValueError: if ``value`` is negative.
        TypeError: if ``value`` is not a real number.
    """
    _validate_number(value)
    if value < 0:
        raise ValueError("cannot take the square root of a negative number")
    return math.sqrt(value)


_OPERATIONS = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "sqrt": sqrt,
}


def calculate(left: Number, operator: str, right: Number | None = None) -> Number:
    """Apply an arithmetic operator, including unary ``sqrt``, to operands."""
    if not isinstance(operator, str) or operator not in _OPERATIONS:
        raise ValueError(f"unsupported operator: {operator!r}")
    if operator == "sqrt":
        if right is not None:
            raise ValueError("sqrt accepts one operand")
        return sqrt(left)
    return _OPERATIONS[operator](left, right)



def main() -> None:
    """Run the calculator command-line interface."""
    parser = argparse.ArgumentParser(description="Perform a basic calculation.")
    parser.add_argument("left", type=float, nargs="?", help="first number")
    parser.add_argument(
        "operator", nargs="?", choices=sorted(_OPERATIONS), help="+ - * / sqrt"
    )
    parser.add_argument("right", type=float, nargs="?", help="second number (omit for sqrt)")
    args = parser.parse_args()

    if args.left is None or args.operator is None:
        parser.error("provide a number and an operator")
    if args.operator == "sqrt":
        if args.right is not None:
            parser.error("sqrt accepts one operand")
    elif args.right is None:
        parser.error("provide a number, an operator, and another number")

    try:
        result = calculate(args.left, args.operator, args.right)
    except (ValueError, ZeroDivisionError) as error:
        parser.error(str(error))
    print(result)


if __name__ == "__main__":
    main()
