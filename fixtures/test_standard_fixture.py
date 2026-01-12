"""
This file holds the practice on using a fixture
"""

import pytest
import logging

log = logging.getLogger(__name__)

@pytest.fixture
def values():
    return [x for x in range(15)]


def test_values(values):
    log.info("Validating standard fixture")
    assert isinstance(values, list)
