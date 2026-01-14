"""
This file holds the practice on fixture level parametrization
"""

import pytest
import logging
import random

log = logging.getLogger(__name__)


@pytest.fixture(params=[11, 22, 35, 66, pytest.param(random.randint(22, 55), 
                                                     marks=[pytest.mark.Regression,
                                                            pytest.mark.xfail(reason="RandomNumberCase")],
                                                     id="random_value_case")])
def value(request):
    return request.param


def test_fixture_based_parametrize(value):
    log.info("Validating fixture based parametrization")
    assert value%11==0
