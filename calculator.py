"""A small command-line calculator."""

import math
import sys


def validate_number(value):
    """Convert *value* to a finite number or raise ValueError."""
    if isinstance(value, bool):
        raise ValueError("boolean values are not valid numbers")
    try:
        number = float(value)
    except (TypeError, ValueError, OverflowError):
        raise ValueError("invalid numeric value: {!r}".format(value))
    if not math.isfinite(number):
        raise ValueError("number must be finite")
    return number


def add(first, second):
    return validate_number(first) + validate_number(second)


def subtract(first, second):
    return validate_number(first) - validate_number(second)


def multiply(first, second):
    return validate_number(first) * validate_number(second)


def divide(first, second):
    numerator = validate_number(first)
    denominator = validate_number(second)
    if denominator == 0:
        raise ZeroDivisionError("cannot divide by zero")
    return numerator / denominator


_OPERATIONS = {
    "+": add,
    "add": add,
    "-": subtract,
    "subtract": subtract,
    "*": multiply,
    "multiply": multiply,
    "/": divide,
    "divide": divide,
}


def main(argv=None):
    """Run the calculator as ``calculator.py OPERATION NUMBER NUMBER``."""
    args = sys.argv[1:] if argv is None else list(argv)
    if len(args) != 3 or args[0].lower() not in _OPERATIONS:
        print("Usage: calculator.py {add|subtract|multiply|divide} NUMBER NUMBER", file=sys.stderr)
        return 2

    try:
        result = _OPERATIONS[args[0].lower()](args[1], args[2])
    except (ValueError, ZeroDivisionError) as error:
        print("Error: {}".format(error), file=sys.stderr)
        return 1

    print(result)
    return 0


if __name__ == "__main__":
    sys.exit(main())
