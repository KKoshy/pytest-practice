"""
This file holds the practice on using pytest.RaisesGroup
"""

import pytest
import logging

log = logging.getLogger(__name__)


def test_raises_group_01():
    log.info("Validating ExceptionGroup with RaisesGroup")
    with pytest.RaisesGroup(ValueError, TypeError):
        raise ExceptionGroup("Testing Exception Group", [ValueError("Not the correct value"), 
                                                         TypeError("Not the correct type")])
    

def test_raises_group_02():
    log.info("Validating ExceptionGroup with RaisesGroup; inspecting object")
    # match parameter is used to validate the group message.
    with pytest.RaisesGroup(ValueError, TypeError, match=r"Testing Exception Group") as reg:
        raise ExceptionGroup("Testing Exception Group", [ValueError("Not the correct value"), 
                                                         TypeError("Not the correct type")])
    assert reg.match(r"Testing Exception Group")
    log.info(f"reg: {reg}")
    log.info(f"reg.traceback: {reg.traceback}")
    log.info(f"reg.type: {reg.type}")
    log.info(f"reg.typename: {reg.typename}")
    
