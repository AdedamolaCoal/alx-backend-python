#!/usr/bin/env python3
"""
This module takes a list of floats and returns their sum as a float
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """_summary_

    Args:
      input_list (list[float]): takes an argument that is a list of floats

    Returns:
      float: returns a float list with the sum of all floats in the list input_list.
    """
    return sum(input_list)
