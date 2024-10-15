#!/usr/bin/env python3
"""
This module contains the async function measure_time
"""
import asyncio
import time

wait_n = __import__("1-concurrent_coroutines").wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    Spawns wait_random n times with the specified max_delay.

    Args:
      n (int): The number of times to spawn wait_random.
      max_delay (int): The maximum delay for each wait_random call.

    Returns:
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - start_time) / n
