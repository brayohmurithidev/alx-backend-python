#!/usr/bin/env python3

'''
The program prints the wait_random function n
number of times and then prints the resulting delay time
as an array in ascending order.
'''
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n:int, max_delay:int) -> List[float]:
    '''
    returns a sorted list of delayed seconds from a random
    generated value
    '''
    # Make sure that n and max_delay are positive integers
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a positive integer")
    if not isinstance(max_delay, int) or max_delay < 0:
        raise ValueError("max_delay must be a positive integer")
    
    list_of_delays = []
    for i in range(n):
        list_of_delays.append(wait_random(max_delay))

    
    results = await asyncio.gather(*list_of_delays)

    for i in range(len(results)):
        for j in range(len(results)):
            # if element at j is smaller than element at i then swap.
            if results[j] < results[i]:
                results[i], results[j] = results[j], results[i]


    return results
        