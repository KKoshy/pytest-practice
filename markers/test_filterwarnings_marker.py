"""
This file holds the practice on using filterwarnings marker
"""

import logging
import pytest
import warnings

log = logging.getLogger(__name__)


def invoke_v1():
    warnings.warn("This method - invoke_v1 - is outdated ; use the latest version - invoke_v2_beta", DeprecationWarning)
    log.info("Invoking v1")
    return True


def invoke_v2_beta1():
    log.info("Invoking v2 beta1")
    return True

def invoke_v2_beta2():
    warnings.warn("Please register your account again", UserWarning)
    log.info("Invoking v2 beta2")
    return True


@pytest.mark.parametrize("version", [invoke_v1, invoke_v2_beta1])
# just show the warning; no failure
@pytest.mark.filterwarnings("always:.* invoke_v1 .* invoke_v2_beta$:DeprecationWarning")
def test_filterwarnings_marker_01(version):
    log.info("Verifying filterwarnings marker with always action")
    assert version()
    log.info("Calling again")
    # calling again raises the warning again.
    assert version()


@pytest.mark.parametrize("version", [invoke_v1, invoke_v2_beta1])
# considers the warning as an error; fails the test case
@pytest.mark.filterwarnings("error:.* invoke_v1 .* invoke_v2_beta$:DeprecationWarning")
def test_filterwarnings_marker_02(version):
    log.info("Validating filterwarnings marker with error action")
    assert version()


@pytest.mark.parametrize("version", [invoke_v1, invoke_v2_beta1])
# ignores the warning as the warning message doesn't match
@pytest.mark.filterwarnings("error:non-matching warning message:DeprecationWarning")
def test_filterwarnings_marker_03(version):
    log.info("Validating filterwarnings marker with error action with non-matching warning message")
    assert version()


@pytest.mark.parametrize("version", [invoke_v1, invoke_v2_beta1])
# raises the warning only once per location even when invoked multiple times
@pytest.mark.filterwarnings("default:.* invoke_v1 .* invoke_v2_beta$:DeprecationWarning")
def test_filterwarnings_marker_04(version):
    log.info("Validating filterwarnings marker with default action")
    assert version()
    log.info("Calling again")
    assert version()


@pytest.mark.parametrize("version", [invoke_v1, invoke_v2_beta1])
# completely suppresses the warning no matter how many times it is raised
@pytest.mark.filterwarnings("ignore:.* invoke_v1 .* invoke_v2_beta$:DeprecationWarning")
def test_filterwarnings_marker_05(version):
    log.info("Validating filterwarnings marker with ignore action")
    assert version()
    log.info("Calling again")
    assert version()


@pytest.mark.parametrize("version", [invoke_v1, invoke_v2_beta2])
# stacking the marker for multiple warnings
@pytest.mark.filterwarnings("default:.* register your account .*:UserWarning")
@pytest.mark.filterwarnings("ignore:.* invoke_v1 .* invoke_v2_beta$:DeprecationWarning")
def test_filterwarnings_marker_06(version):
    log.info("Validating filterwarnings marker with multiple warnings")
    assert version()
    log.info("Calling again")
    assert version()
