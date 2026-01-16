"""
Provides a minimal interface for weight calculation
"""

import logging

log = logging.getLogger(__name__)


G=9.8


def calculate_weight(mass: float) -> float:
    log.info(f"Calculating weight for mass value: {mass}")
    return mass*G
