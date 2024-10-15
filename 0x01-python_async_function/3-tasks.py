#!/usr/bin/env python3

import asyncio

wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Spawns wait_random with the specified max_delay.

    Args:
      max_delay (int): The maximum delay in seconds.

    Returns:
      asyncio.Task: The spawned task.
    """
    return asyncio.create_task(wait_random(max_delay))
