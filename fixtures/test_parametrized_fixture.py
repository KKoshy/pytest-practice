"""
This file holds the practice on using parametrized fixture
"""

import pytest
import logging

log = logging.getLogger(__name__)


@pytest.fixture(params=[x for x in range(1, 7)])
def value(request):
    return request.param**2

def test_parametrized_fixture(value):
    assert isinstance(value, int)
