"""
This file holds the practice on assertions for raised exceptions
"""

import pytest
import logging

log = logging.getLogger(__name__)


def create_value_error():
    raise ValueError("Not the correct value now either")

def test_raises_01():
    log.info("Validating raises with pytest")
    with pytest.raises(ValueError):
        raise ValueError("Not the correct value")
    

def test_raises_02():
    log.info("Validating raises with pytest; inspecting the object")
    with pytest.raises(ValueError, match=r".* correct value now either$") as ve:
        create_value_error()
    log.info(f"{ve}, {ve.traceback}, {ve.type}, {ve.value}")
    assert ve.type is ValueError
    # another way to match the value
    assert ve.match(r".* correct value now either$")
