"""A small dependency-free calculator.

The public arithmetic functions operate on numbers, while
:func:`evaluate_expression` accepts simple arithmetic expressions containing
numbers, parentheses, and the operators ``+``, ``-``, ``*``, and ``/``.
"""

from __future__ import annotations

import ast
import operator
import sys
from numbers import Real
from typing import Union

Number = Union[int, float]


def _validate_number(value: Number) -> None:
    """Raise TypeError when *value* is not a real number."""
    if isinstance(value, bool) or not isinstance(value, Real):
        raise TypeError("operands must be real numbers")


def add(left: Number, right: Number) -> Number:
    """Return the sum of two real numbers."""
    _validate_number(left)
    _validate_number(right)
    return left + right


def subtract(left: Number, right: Number) -> Number:
    """Return the difference between two real numbers."""
    _validate_number(left)
    _validate_number(right)
    return left - right


def multiply(left: Number, right: Number) -> Number:
    """Return the product of two real numbers."""
    _validate_number(left)
    _validate_number(right)
    return left * right


def divide(left: Number, right: Number) -> float:
    """Return ``left / right``.

    Division by zero is deliberately exposed as ``ZeroDivisionError`` with a
    stable, user-friendly message.
    """
    _validate_number(left)
    _validate_number(right)
    if right == 0:
        raise ZeroDivisionError("cannot divide by zero")
    return left / right


_BINARY_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
}
_UNARY_OPERATORS = {ast.UAdd: operator.pos, ast.USub: operator.neg}


def _evaluate_node(node: ast.AST) -> Number:
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) \
            and not isinstance(node.value, bool):
        return node.value

    if isinstance(node, ast.UnaryOp) and type(node.op) in _UNARY_OPERATORS:
        return _UNARY_OPERATORS[type(node.op)](_evaluate_node(node.operand))

    if isinstance(node, ast.BinOp) and type(node.op) in _BINARY_OPERATORS:
        left = _evaluate_node(node.left)
        right = _evaluate_node(node.right)
        if isinstance(node.op, ast.Div) and right == 0:
            raise ZeroDivisionError("cannot divide by zero")
        return _BINARY_OPERATORS[type(node.op)](left, right)

    raise ValueError("invalid expression; use numbers and +, -, *, / only")


def evaluate_expression(expression: str) -> Number:
    """Evaluate a simple arithmetic expression without executing code."""
    if not isinstance(expression, str) or not expression.strip():
        raise ValueError("expression must be a non-empty string")

    try:
        tree = ast.parse(expression, mode="eval")
    except (SyntaxError, ValueError, TypeError) as exc:
        raise ValueError("invalid expression") from exc
    return _evaluate_node(tree.body)


# A descriptive alias for callers that prefer the longer name.
calculate_expression = evaluate_expression


def main() -> None:
    """Read one expression from standard input and print its result."""
    expression = input("Expression: ")
    try:
        print(evaluate_expression(expression))
    except (ValueError, ZeroDivisionError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
