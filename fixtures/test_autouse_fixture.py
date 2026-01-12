"""
This file holds the practice on using autouse fixture
"""

import pytest
import logging

log = logging.getLogger(__name__)

@pytest.fixture
def values():
    return [1, 2]

@pytest.fixture(autouse=True)
def update(values):
    values.extend([3, 4, 5])


def test_autouse_01(values):
    log.info("Validating autouse - method 01")
    values.append(6)
    assert values == [x for x in range(1, 7)]

def test_autouse_02(values):
    # modifying in the above test method wouldn't impact the fixture
    log.info("Validating autouse - method 02")
    assert values == [x for x in range(1, 6)]
