"""
This file holds the practice on adding dynamic scope to a fixture
"""

import pytest
import logging

log = logging.getLogger(__name__)


def determine_scope(fixture_name, config):
    log.info(f"fixture: {fixture_name}")
    log.info(f"config: {config}")
    # getoption will not register option when specified in CLI;
    # it should be registered as part of pytest_addoption 
    scope = config.getoption("--scope", "function")
    log.info(f"scope considered: {scope}")
    return scope

@pytest.fixture(scope=determine_scope, params=[1, 2, 3])
def values(request):
    return request.param


def test_dynamic_scope_01(values):
    log.info(values)
    assert values


def test_dynamic_scope_02(values):
    log.info(values)
    assert values
