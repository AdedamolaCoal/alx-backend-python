#!/usr/bin/env python3
"""Returns an async generator."""

import asyncio
import random


async def async_generator():
    """
    A coroutine that asynchronously loop 10 times and returns a random async generator between 0 and 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)