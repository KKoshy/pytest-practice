"""
This file holds the practice on marker based parametrization
"""

import logging
import pytest
import random

log = logging.getLogger(__name__)


def gen_id(val):
    return f"num{val}"

def validate_input(val):
    if val<0:
        raise ValueError(f"Negative value: {val}")
    else:
        log.info(f"Proceeding with the value: {val}")


@pytest.mark.parametrize("x,y", [(1, 1), (2, 2)], ids=["once", "twice"])
def test_marker_parametrize_01(x, y):
    log.info("Validating marker based parametrization with ids")
    assert x == y

@pytest.mark.parametrize("x,y", [(1, 1), (2, 2)], ids=gen_id)
def test_marker_parametrize_02(x, y):
    log.info("Validating marker based parametrization with callable id generation")
    assert x == y


@pytest.mark.parametrize("x,y", [(1, 1), (2, 4), 
                                 pytest.param(3, random.randint(1, 4)**2, 
                                              marks=pytest.mark.xfail(reason="Random generation failure"), 
                                              id="random_gen"), 
                                 pytest.param(random.randint(-2, 2), random.randint(-0, 4),
                                              marks=[pytest.mark.xfail(raises=ValueError, reason="Failing for negative values"),
                                                     pytest.mark.Regression,
                                                     pytest.mark.Plv],
                                              id="negative_value")])
def test_marker_parametrize_03(x, y):
    validate_input(x)
    log.info("Validating marker based parametrization with pytest.param")
    assert x**2 == y
