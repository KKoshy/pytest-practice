"""
Provides a minimal Atom class for testing
"""
class Atom:
    def __init__(self, value: int, element: str) -> None:
        self.atomic_number = value
        self.element = element

    def __eq__(self, other: Atom) -> bool:
        return self.atomic_number==other.atomic_number
