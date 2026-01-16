"""
This file holds the practice on function mocking
"""

import logging
import pytest
from lib.file_actions import create_file, delete_file
from pytest_mock import MockFixture

log = logging.getLogger(__name__)


@pytest.mark.dependency(name='create')
def test_file_creation(mocker: MockFixture):
    log.info("Validating mocking of a function - 01")
    mock = mocker.patch("builtins.open")
    create_file("file.txt", "Hello, how do you do?")
    mock.assert_called_once()
    mock.assert_called_once_with("file.txt", "w+")

@pytest.mark.dependency(depends=['create'])
def test_file_deletion(mocker: MockFixture):
    log.info("Validating mocking of a function - 02")
    mock = mocker.patch("os.remove")
    delete_file("file.txt")
    mock.assert_called_once()
    mock.assert_called_with("file.txt")
