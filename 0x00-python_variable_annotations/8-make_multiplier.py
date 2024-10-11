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

    def inner(n: float) -> float:
        multiply: float = n * multiplier
        return multiply

    return inner
