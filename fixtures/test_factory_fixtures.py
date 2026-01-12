"""
This file holds the practice on using factory fixtures
"""

import pytest
import random
import logging

log = logging.getLogger(__name__)


@pytest.fixture
def user_log():
    def generate_log(user):
        user_log = {"user": user, "dice": random.randint(1, 6)}
        log.info(f"user_log: {user_log}")
        return user_log
    return generate_log


def test_factory_fixture(user_log):
    # regular fixtures cache the results
    # when the same fixture has to be requested multiple times
    # factory fixture is useful
    log.info("Validating factories as fixtures")
    assert user_log("Al").get("dice") <=6
    assert user_log("Simon").get("dice") <=6
    assert user_log("Theodore").get("dice") <=6
