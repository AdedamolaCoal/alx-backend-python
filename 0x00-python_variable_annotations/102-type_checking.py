#!/usr/bin/env python3
"""Returns a new list where each element is repeated 'factor' times."""

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Zooms into the array by repeating each element 'factor' times.

    Parameters:
    lst (Tuple): A tuple of any elements.
    factor (int): The factor by which to zoom. Defaults to 2.

    Returns:
    List: A new list where each element is repeated 'factor' times.
    """
    zoomed_in: List = [item for item in lst for i in range(factor)]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)
zoom_3x = zoom_array(array, 3)
