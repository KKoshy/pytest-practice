"""
This file holds the practice on marker based indirect parametrization for specific values
"""

import logging
import pytest

log = logging.getLogger(__name__)


@pytest.fixture
def x(request):
    return request.param*3


@pytest.fixture
def y(request):
    return request.param*2


@pytest.mark.parametrize(argnames="x,y,expected", 
                         argvalues=[("a", "b", "aaab"), ("c", "d", "cccd")],
                         indirect=["x"],
                         ids=["case-01", "case-02"])
def test_indirect_specific_parametrize(x, y, expected):
    log.info("Validating application of indirect on some arguments only")
    assert x+y == expected
