#!/usr/bin/env python3
"""
6-sum_mixed_list
This module takes a list of both ints and floats and returns their sum as a float
"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """_summary_

    Args:
      mxd_list (list[Union[int, float]]): takes an argument that is a list of
      both ints and floats

    Returns:
      float: returns a float list with the sum of all floats and ints in the list mxd_list.
    """
    return sum(mxd_list)
