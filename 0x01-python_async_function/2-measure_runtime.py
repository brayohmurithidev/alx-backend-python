#!/usr/bin/env python3

'''
A function that calculate the elapsed execution time
'''

import asyncio
wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''
    import time and separate start time from elapsed time
    '''
    import time
    # Refence point time is initialized to variable s
    s = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    # elapesed time is calculated as time taken to execute - initial time.
    total_time = time.perf_counter() - s

    return total_time / n
