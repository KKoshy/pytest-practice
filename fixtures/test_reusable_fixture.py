"""
This file holds the practice on reusing fixtures
"""

import logging
import pytest

log = logging.getLogger(__name__)

@pytest.fixture
def first_entry():
    return 1

@pytest.fixture
def values(first_entry):
    return [first_entry]


def test_reusable_01(values):
    log.info("Validating reusable fixtures - method 01")
    values.append(45)
    assert values == [1, 45]


def test_reusable_02(values):
    log.info("Validating reusable fixtures - method 02")
    # values from the first method is not cached
    values.append("a")
    assert values == [1, "a"]
