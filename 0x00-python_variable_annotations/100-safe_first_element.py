#!/usr/bin/env python3
"""Checks if the list is empty"""

from typing import Sequence, Any, Union, Optional


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """_summary_

    Args:
        lst (Sequence[Any]): checks the first element of a list

    Returns:
        Optional[Any]: returns the first element of a list if present and None otherwise
    """
    if lst:
        return lst[0]
    else:
        return None
