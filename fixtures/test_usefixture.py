"""
This file holds the practice on using usefixture marker
"""

import pytest
import logging

log = logging.getLogger(__name__)


@pytest.fixture
def add_first():
    log.info("Adding first logger")

@pytest.fixture
def add_second():
    log.info("Adding second logger")


@pytest.mark.usefixtures("add_first", "add_second")
class TestUsefixture:
    def test_usefixture_01(self):
        log.info("Validating usefixture - 01")


    def test_usefixture_02(self):
        log.info("Validating usefixture - 02")
