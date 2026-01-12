"""
This file holds the practice on adding data to a fixture from test marker
"""

import pytest
import logging

log = logging.getLogger(__name__)


@pytest.fixture
def values(request):
    data = [1, 2, 3, 4]
    marker = request.node.get_closest_marker("set_data")
    if marker:
        data.append(marker.args[0])
    log.info(f"currently data is {data}")
    return data


@pytest.mark.set_data(45)
def test_adding_data_with_markers_01(values):
    log.info("Validating addition of data to fixture from a marker - 02")
    assert values == [1, 2, 3, 4, 45]


@pytest.mark.set_data(76)
def test_adding_data_with_markers_02(values):
    log.info("Validating addition of data to fixture from a marker - 02")
    assert values == [1, 2, 3, 4, 76]
