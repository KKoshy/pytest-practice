"""
This file holds the practice on Conftest hook for adding pytest configuration options
"""

import logging
from pytest import Config

log = logging.getLogger(__name__)


def pytest_configure(config: Config):
    # this hook is added before logging is configured;
    # hence the log statement would not work and so print is used
    print("Adding config values")
    # registers the marker and avoids the PytestUnknownMarkWarning warning
    config.addinivalue_line(
        "markers", "Regression: Covering Regression tests"
    )
    
