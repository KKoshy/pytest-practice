"""
This file holds the practice on marker based indirect parametrization
"""

import logging
import pytest

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
def version(request):
    if request.param == "v1":
        return V1()
    elif request.param == "v2_beta1":
        return V2Beta1()
    else:
        return V2Beta2()
    

@pytest.mark.parametrize("version", ["v1", "v2_beta1", "v2_beta2", "v2"], indirect=True)
def test_indirect_parametrize(version):
    log.info("Validating parametrization with indirect")
    log.info(f"verion: {version}")
    assert version.support_dark_theme()
    
