#!/usr/bin/env python3
"""This module contains the async function wait_random"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Returns the random float"""
    ans = random.uniform(0, max_delay)
    await asyncio.sleep(ans)
    return ans
