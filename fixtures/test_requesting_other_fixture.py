"""
This file holds the practice on implementing fixture requesting a fixture
"""

import pytest
import logging

log = logging.getLogger(__name__)


@pytest.fixture
def first_entry():
    return 1

@pytest.fixture
def values(first_entry):
    return [first_entry]


def test_fixture_requesting_fixture(values):
    log.info("Validating fixture requesting another fixture")
    assert values == [1]
