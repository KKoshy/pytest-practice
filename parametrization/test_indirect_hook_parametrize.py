"""
This file holds the practice on pytest hook based indirect parametrization
"""

import pytest
import logging

log = logging.getLogger(__name__)


class V1:
    def support_dark_theme(self):
        log.info("Dark theme not supported")
        return False


class V2Beta1:
    def support_dark_theme(self):
        log.info("Dark theme enabled!")
        return True


class V2Beta2:
    def support_dark_theme(self):
        log.info("Dark theme enabled; you can now create custom themes!")
        return True


@pytest.fixture
def theme_version(request):
    if request.param == "v1":
        return V1()
    elif request.param == "v2_beta1":
        return V2Beta1()
    else:
        return V2Beta2()
    

def test_hook_indirect_parametrize(theme_version):
    log.info("Validating indirect hook based parametrization")
    log.info(f"version: {theme_version}")
    assert theme_version.support_dark_theme()
