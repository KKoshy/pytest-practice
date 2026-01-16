"""
This file holds the practice on variable mocking
"""

import logging
from lib.weights import calculate_weight
from pytest_mock import MockFixture


log = logging.getLogger(__name__)


def test_weight_calculation(mocker: MockFixture):
    log.info("Validating mocking of a variable")
    # G is a variable; hence it will not have return value
    # even if a mock object is created, it will not have assert methods associated,
    # since only a variable is mocked here.
    mocker.patch("lib.weights.G", new=3.59)
    assert calculate_weight(3) == 10.77
