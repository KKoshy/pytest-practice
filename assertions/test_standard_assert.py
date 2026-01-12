"""
This file holds the practice on Standard assert
"""

def seventh_table(x):
    return 7*x


def test_values():
    assert seventh_table(3) == 35, "Incorrect seventh table value"
