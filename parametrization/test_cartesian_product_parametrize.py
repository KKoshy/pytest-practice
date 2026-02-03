"""
This file holds the practice on cartesian product based parametrization for tests with
multiple fixtures
"""

import pytest
import logging

log = logging.getLogger(__name__)


@pytest.fixture(params=[x for x in range(1, 7)])
def box_01(request):
    return request.param


@pytest.fixture(params=[x for x in range(1, 3)])
def box_02(request):
    return request.param


@pytest.fixture(params=[2*x for x in range(1, 3)])
def box_03(request):
    return request.param

# Following test will be executed 12 times
@pytest.mark.UnequalParams
def test_cartesian_product_parametrize_01(box_01, box_02):
    log.info("Validating cartesina product parametrization " \
    "when fixtures have different number of param values")
    assert box_01*box_02 > 0

# Following test will be executed 4 times 
@pytest.mark.EqualParams
def test_cartesian_product_parametrize_02(box_02, box_03):
    log.info("Validating cartesina product parametrization " \
    "when fixtures have different number of param values")
    assert box_02*box_03 > 0

