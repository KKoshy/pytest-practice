"""
Provides a minimal set of file actions for testing
"""

import os
import logging

log = logging.getLogger(__name__)


def create_file(file_name: str, content: str):
    log.info(f"Creating file: {file_name}")
    with open(file_name, "w+") as f:
        f.write(content)

def delete_file(file_name: str):
    log.info(f"Deleting file: {file_name}")
    os.remove(file_name)
