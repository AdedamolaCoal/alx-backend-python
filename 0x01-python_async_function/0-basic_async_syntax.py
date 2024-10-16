#!/usr/bin/env python3
"""This module contains the async function wait_random"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and max_delay
    (included and float value) seconds and eventually returns it.

    Args:
        max_delay (int): The maximum delay in seconds. Defaults to 10.

    Returns:
        float: The random delay in seconds.
    """
    ans = random.random() * max_delay
    await asyncio.sleep(ans)
    return ans
