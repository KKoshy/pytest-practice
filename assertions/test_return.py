"""
This file holds the practice on using return statement in a test method
"""
import logging

log = logging.getLogger(__name__)


def test_return_value():
    log.info("Adding return to pytest test function")
    # case passes but causes PytestReturnNotNoneWarning warning
    return 1+2
