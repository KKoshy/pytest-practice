"""
This file holds the practice on using usefixture marker
"""

import pytest
import logging

log = logging.getLogger(__name__)

@pytest.fixture
def add_log():
    log.info("Pytest initiated testing sequence")

@pytest.fixture
def second_log():
    log.info("Initiating secondary log")

@pytest.mark.usefixtures("add_log", "second_log")
def test_usefixture_marker():
    log.info("Validating usefixture marker")
    assert isinstance([x for x in range(5)], list)
