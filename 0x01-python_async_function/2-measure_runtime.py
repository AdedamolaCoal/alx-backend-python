#!/usr/bin/env python3
"""Returns the total time it takes to run wait_n"""

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
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()
    total_time = (end_time - start_time) / n
    return total_time
