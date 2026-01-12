"""
This file holds the practice for caching results of a fixture
"""

import pytest
import logging

log = logging.getLogger(__name__)


@pytest.fixture
def initial_value():
    return [1, 2, 3]

@pytest.fixture
def values(initial_value):
    initial_value.append(335)
    return initial_value

def test_multi_requests_fixture(values, initial_value):
    # important
    # fixtures requested more than once in a test are not executed more than once per test
    # the results are cached and reused instead
    log.info("Verifying that fixtures are executed once per test and their return values are cached")
    assert values == initial_value
