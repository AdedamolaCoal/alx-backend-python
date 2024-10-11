#!/usr/bin/env python3
"""returns a multiplier of the input"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by a multiplier.

    Args:
      multiplier (float): takes an argument that is a float

    Returns:
      Callable[[float], float]: returns a function that multiplies a float by a multiplier.
    """

    def multiply(n: float) -> float:
        """The inner multiplier"""
        return n * multiplier

    return multiply
