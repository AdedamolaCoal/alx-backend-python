#!/usr/bin/env python3
"""Returns the key value from a mapping if available, otherwise the default value"""

from types import NoneType
from typing import TypeVar, Mapping, Any, Union

T = TypeVar("T")


def safely_get_value(
    dct: Mapping[Any, Any], key: Any, default: Union[T, NoneType]
) -> Union[Any, T]:
    """
    Safely retrieve a value from a mapping.

    If the key is present in the mapping, return its value. Otherwise, return the
    default value.

    Args:
        dct: The mapping to retrieve the value from.
        key: The key to look up in the mapping.
        default: The value to return if the key is not present in the mapping.

    Returns:
        The value associated with the key if it is present, or the default value.
    """
    if key in dct:
        return dct[key]
    return default
