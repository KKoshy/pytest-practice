"""
This file holds the practice on Conftest configuration for adding CLI options
"""

import logging

log = logging.getLogger(__name__)


def pytest_addoption(parser):
    # this is a pytest hook
    # used to register a CLI option
    log.info("Parsing options")
    parser.addoption("--scope", 
                     action="store", 
                     default="function", 
                     help="Specify scope for the test method",
                     choices=("function", "module"))
    
