"""
This file holds the practice on standard mocking
"""

import logging
import math
from pytest_mock import MockFixture

log = logging.getLogger(__name__)


def test_mocking(mocker: MockFixture):
    log.info("Testing mocking with mocker fixture")
    mock = mocker.patch("math.sqrt", return_value=20)
    value = math.sqrt(36)
    assert value==20
    mock.assert_called_once()
