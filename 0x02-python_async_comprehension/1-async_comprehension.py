#!/usr/bin/env python3
"""Generates a list of 10 random
numbers using async comprehension module.
"""

from typing import List

# from importlib import import_module as using

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using
    async comprehension over async_generator.
    """
    value = [i async for i in async_generator()]
    return value
