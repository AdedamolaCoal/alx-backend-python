#!/usr/bin/env python3

import time
import asyncio

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
    Measures the runtime of async_comprehension
    """
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.perf_counter()
    return end - start
