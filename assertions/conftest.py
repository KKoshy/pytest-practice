"""
This file holds the practice on Conftest configuration for custom assertion introspection
"""
from lib.atom import Atom

def pytest_assertrepr_compare(op, left, right):
    if isinstance(left, Atom) and isinstance(right, Atom) and op=="==":
        return [
            "Failed: not the same elements",
            f"left: {left.atomic_number, left.element}",
            f"right: {right.atomic_number, right.element}"
        ]
