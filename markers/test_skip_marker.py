"""
This file holds the practice on using skip marker
"""

import pytest
import logging

log = logging.getLogger(__name__)


@pytest.fixture
def values():
    return [x for x in range(5)]


@pytest.mark.skip(reason="Skipping due to Jira-112233")
def test_skip_marker(values):
    log.info("Validating skip marker")
    assert isinstance(values, list)
