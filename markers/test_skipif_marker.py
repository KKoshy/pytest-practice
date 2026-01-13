"""
This file holds the practice on using skipif marker
"""

import pytest
import logging
import sys

log = logging.getLogger(__name__)

def platform():
    return "linux" in sys.platform

@pytest.fixture
def upgrade_versions():
    return [x for x in range(5)]


@pytest.mark.skipif(condition=platform(), reason="Skipping due to wrong platform")
def test_skipif_marker(upgrade_versions):
    log.info("Validating skipif marker")
    assert isinstance(upgrade_versions, list)
