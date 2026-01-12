"""
This file holds the practice on using pytest.approx()
"""

import pytest
import logging

log = logging.getLogger(__name__)

def test_value_01():
    log.info("Verifying float without approx")
    assert 0.1+0.2 == 0.3


def test_value_02():
    log.info("Verifying float with approx")
    assert 0.1+0.2 == pytest.approx(0.3)


def test_value_03():
    log.info("Validating float tuple without approx")
    assert (0.1+0.2, 0.2+0.4) == (0.3, 0.6)


def test_value_04():
    log.info("Validating float tuple with approx")
    assert (0.1+0.2, 0.2+0.4) == pytest.approx((0.3, 0.6))


def test_value_05():
    log.info("Validating float based dict without approx")
    assert {"key01": 0.1+0.2, "key02": 0.2+0.4} == {"key01": 0.3, "key02": 0.6}

def test_value_06():
    log.info("Validating float based dict with approx")
    assert {"key01": 0.1+0.2, "key02": 0.2+0.4} == pytest.approx({"key01": 0.3, "key02": 0.6})
