#!/usr/bin/env python3
from typing import List, Union


def sum_numbers_in_list(numbers: List[Union[int, float]]) -> float:
    """
    Returns the sum of all numbers in the input list.

    Args:
        numbers: A list of integers and/or floats.

    Returns:
        The sum of all numbers in the list as a float.

    Raises:
        TypeError: If the input is not a list.
        ValueError: If the list contains non-numeric values.
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    if not all(isinstance(x, (int, float)) for x in numbers):
        raise ValueError("List must only contain numbers")
    if not numbers:
        raise ValueError("List cannot be empty")
    return float(sum(numbers))
