"""
This file holds the practice on class level parametrization
"""

import logging
import pytest

log = logging.getLogger(__name__)

@pytest.fixture()
def x(request):
    return request.param*7


@pytest.mark.parametrize(argnames="x,y", 
                         argvalues=[(1, 7), (2, 14)], 
                         indirect=["x"],
                         ids=["case-01", "case-02"],
                         scope="class")
class TestValues:

    def test_values_01(self, x, y):
        log.info("Validating class level parametrization - 01")
        assert x==y

    def test_value_02(self, x, y):
        log.info("Validating class level parametrization - 02")
        assert x%7==0


