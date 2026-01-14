"""
This file holds the practice on Conftest hook for adding parametrization with 
pytest_generate_tests
"""

import logging
from pytest import Metafunc

log = logging.getLogger(__name__)


def pytest_generate_tests(metafunc: Metafunc):
    log.info("Parametrizing test cases")
    if "value_01" in metafunc.fixturenames:
        metafunc.parametrize(argnames="value_01", argvalues=[x for x in range(3)])

    if "theme_version" in metafunc.fixturenames:
        metafunc.parametrize(argnames="theme_version", argvalues=["v1", "v2_beta1", "v2_beta2", "v2"], indirect=True)

    if "version01" in metafunc.fixturenames and "version02" in metafunc.fixturenames:
        metafunc.parametrize(argnames="version01, version02", 
                             argvalues=[(1.0, 1.0), (2.0, 2.0)],
                             ids=["case-01", "case-02"])
