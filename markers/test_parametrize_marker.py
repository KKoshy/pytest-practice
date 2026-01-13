"""
This file holds the practice on using parametrize marker
"""

import logging
import pytest

log = logging.getLogger(__name__)


def gen_id(val):
    return f"seventh{val}"


@pytest.mark.parametrize("x,y,z", [(2, 3, 6), (3, 4, 12), (4, 5, 20), (3, 2, 6)])
def test_parametrize_marker_01(x, y, z):
    log.info("Validating parametrization with multiple values")
    assert x*y == z

@pytest.mark.parametrize("x,z", [(1, 7), (2, 14), (3, 21), (4, 28)], 
                         ids=["seventh1", "seventh2", "seventh3", "seventh4"])
def test_parametrize_marker_02(x, z):
    log.info("Validating parametrization with ids")
    assert 7*x == z

# callable with only receive one param value at a time formatting each param.
# before applying callable, id would be in the form -> [param1-param2-param3...]
# after applying callable, id would be in the form -> [func(param1)-func(param2)-func(param3)...]
@pytest.mark.parametrize("x,z", [(1, 7), (2, 14), (3, 21), (4, 28)], ids=gen_id)
def test_parametrize_marker_03(x, z):
    log.info("Validating parametrization with ids with a callable")
    assert 7*x == z


