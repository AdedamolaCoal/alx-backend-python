#!/usr/bin/env python3
"""Generates a set of random numbers
between 0 and 10 using an async generator.
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    A coroutine that asynchronously loop 10 times and
    returns a random async generator between 0 and 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
