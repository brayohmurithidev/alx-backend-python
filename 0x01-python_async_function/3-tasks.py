#!/usr/bin/env python3

'''
A function that creates a task from the wait random.
'''
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''The function returns the task'''
    return asyncio.create_task(wait_random(max_delay))
