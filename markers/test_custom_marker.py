"""
This file holds the practice on using custom markers
"""

import logging
import pytest

log = logging.getLogger(__name__)


# custom markers have to be registered in pytest.ini file to avoid warnings
# otherwise raises PytestUnknownMarkWarning warning
@pytest.mark.Smoke
def test_custom_marker_01():
    log.info("Validating custom marker - 01 - smoke")


# adding --strict-markers raises errors for test methods with unregistered markers
# without this option, just the PytestUnknownMarkWarning warning is raised
@pytest.mark.Plv
def test_custom_marker_02():
    log.info("Validating custom marker - 02 - Plv")


# markers can also be registered from conftest file
@pytest.mark.Regression
def test_custom_marker_03():
    log.info("Validating custom marker - 03 - Regression")

