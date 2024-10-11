#!/usr/bin/env python3
"""Sums a list of mixed ints and floats."""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """Returns the sum of all numbers in the input list.

    Args:
      mxd_list: takes an argument that is a list of both ints and floats

    Returns:
      float: returns a float with the sum of all floats and ints in the list mxd_list.
    """
    return float(sum(mxd_list))
