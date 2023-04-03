#!/usr/bin/env python3

'''
A program that demos the async await, the await time is a
float generated from a random uniform module.
'''
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    '''Assign variable x to a random float and set it
    as wait time then return it'''
    # print("Code execution starts")
    x = random.uniform(0, max_delay)
    await asyncio.sleep(x)
    # print("Code execution finished")

    return x
