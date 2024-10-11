#!/usr/bin/env python3
"""Returns the first element in a sequence, otherwise None"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """_summary_

    Args:
        lst (Sequence[Any]): A sequence of elements of type any

    Returns:
        Union[Any, None]: The first element if available, otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None
