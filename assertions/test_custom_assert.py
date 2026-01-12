"""
This file holds the practice on custom assert explanations
"""

import logging
from lib.atom import Atom

log = logging.getLogger(__name__)

def test_elements_01():
    element_01 = Atom(17, "Cl")
    element_02 = Atom(17, "Cl")
    assert element_01 == element_02


def test_elements_02():
    element_01 = Atom(17, "Cl")
    element_02 = Atom(1, "H")
    assert element_01 == element_02
