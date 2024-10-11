#!/usr/bin/env python3
"""Returns the appropriate length and type of the element of a list"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns the appropriate length and type of the element of a list"""
    return [(i, len(i)) for i in lst]
