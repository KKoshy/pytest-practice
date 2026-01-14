"""
This file holds the practice on pytest hook based indirect parametrization for multiple values
"""

import logging

log = logging.getLogger(__name__)


def test_multiple_values_hook_parametrize(version01, version02):
    log.info("Validating parametrizing multiple values from hook")
    assert version01==version02
