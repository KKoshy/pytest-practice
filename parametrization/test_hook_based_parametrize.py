"""
This file holds the practice on pytest hook based parametrization
"""

import logging

log = logging.getLogger(__name__)


def test_hook_parametrize(value_01):
    log.info("Validating hook based parametrization")
    assert isinstance(value_01, int)
