"""
This file holds the practice on using xfail marker
"""

import logging
import random
import pytest

log = logging.getLogger(__name__)


def determine_failure():
    value = random.randint(1, 100)
    if value>=50:
        raise ExceptionGroup("Failing due to incorrect version", [ValueError("Incorrect value"), 
                                                                  SystemError("Crashed due to SystemError")])
    
    else:
        return True


@pytest.mark.xfail(reason="Intermittent issue with random generation")
def test_xfail_marker_01():
    log.info("Validating standard xfail marker")
    value = random.randint(1, 100)
    assert value>=50

@pytest.mark.xfail(raises=ZeroDivisionError, reason="Intermittent ZeroDivisionError")
@pytest.mark.parametrize("value", [3, 0])
def test_xfail_marker_02(value):
    log.info("Validating xfail marker with raises")
    assert 100/value

@pytest.mark.xfail(raises=pytest.RaisesGroup(ValueError, SystemError, match=".* incorrect version$"),
                   reason="Intermittent ExceptionGroup errors")
def test_xfail_marker_03():
    log.info("Validating xfail marker with RaisesGroup")
    assert determine_failure()


@pytest.mark.xfail(raises=pytest.RaisesGroup(pytest.RaisesExc(ValueError, match="Incorrect value"),
                                             pytest.RaisesExc(SystemError, match=r".* SystemError$"),
                                             match=r".* incorrect version$"),
                    reason="Intermittent ExceptionGroup errors")
def test_xfail_marker_04():
    log.info("Validating xfail marker with RaisesExc")
    assert determine_failure()
