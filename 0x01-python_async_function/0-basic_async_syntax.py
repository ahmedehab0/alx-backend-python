#!/usr/bin/python3
"""the basic of async"""

import random
import asyncio


async def wait_random(max_delay: int =10) -> float:
    """an asynckronous coroutine function"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
