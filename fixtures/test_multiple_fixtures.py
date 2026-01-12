"""
This file holds the practice on using multiple fixtures
"""

import pytest
import logging


log = logging.getLogger(__name__)

@pytest.fixture
def first_entry():
    return 1

@pytest.fixture
def second_entry():
    return 2

@pytest.fixture
def values(first_entry, second_entry):
    return [first_entry, second_entry]


@pytest.fixture
def expected():
    return [1, 2, 3]


def test_multiple_fixture_usage(values, expected):
    log.info("Validating multiple fixture usage")
    values.append(3)
    assert values == expected
