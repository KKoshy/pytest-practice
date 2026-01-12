"""
This file holds the practice on using parametrized fixture with markers
"""

import pytest
import logging

log = logging.getLogger(__name__)


@pytest.fixture(params=[1, 
                        2, 
                        3, 
                        pytest.param(45, marks=pytest.mark.skip(reason="skipping due to Jira-112233")),
                        pytest.param(97, marks=pytest.mark.xfail(raises=ValueError)),
                        pytest.param(91, marks=pytest.mark.xfail(raises=SystemError))
                        ])
def value(request):
    log.info(request.param)
    return request.param


def test_parametrized_with_marks_fixture(value):
    log.info("\nValidating parametrization with markers in fixture")
    if value == 97:
        raise ValueError("Raising value error")
    assert value
