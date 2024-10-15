#!/usr/bin/env python3
"""Returns an async generator of 10 random numbers using async comprehension."""

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension():
    """
    Collects 10 random numbers using async comprehension over async_generator.

    Args: takes no argument

    Returns: A list of 10 random numbers
    """
    value = [_ async for _ in async_generator()]
    return value
