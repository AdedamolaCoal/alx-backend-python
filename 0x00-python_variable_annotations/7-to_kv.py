#!/usr/bin/env python3
"""returns a tuple"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple with the input string and the square of the input int/float.

    Args:
        k (str): The input string.
        v (int or float): The input integer or float.

    Returns:
        Tuple[str, float]: A tuple with the input string and the square of the input int/float.
    """
    return k, float(v**2)
