"""
This file holds the practice on xfailing cases with specific exceptions and exception messages
"""

import pytest
import logging

log = logging.getLogger(__name__)


@pytest.mark.xfail(raises=ValueError)
def test_xfail_01():
    log.info("Adding xfail based on an exception")
    raise ValueError("Not the correct value")

@pytest.mark.xfail(raises=pytest.raises(ValueError, match=r".* the correct value$"))
def test_xfail_02():
    log.info("Adding xfail based on an exception and its message")
    raise ValueError("Not the correct value")

@pytest.mark.xfail(raises=pytest.raises(ValueError, match=r".* the correct value$"))
def test_xfail_03():
    log.info("Failing with incorrect exception message")
    raise ValueError("Adding the wrong value")

@pytest.mark.xfail(raises=pytest.RaisesGroup(ValueError, RuntimeError, match=r"For testing"))
def test_xfail_04():
    log.info("Adding xfail based on an exception group and its message")
    raise ExceptionGroup("For testing", [ValueError("ve"), RuntimeError("re")])

@pytest.mark.xfail(raises=pytest.RaisesGroup(ValueError, RuntimeError, match=r"Not for testing"))
def test_xfail_05():
    log.info("Failing with incorrect exception group message")
    raise ExceptionGroup("For testing", [ValueError("ve"), RuntimeError("re")])
