#!/usr/bin/env python3

# if we want, we can create a ThreadPoolExecutor
# this creates a pool of threads that can be reused for our functions
# we can then submit our functions to the executor
# it'll return a "future object," which will (eventually) have the result

# the style of using ThreadPoolExecutor is more elegant and easier to understand

from concurrent.futures import ThreadPoolExecutor, wait

def square(n):
    return n ** 2

with ThreadPoolExecutor(max_workers=10) as executor:
    all_results = []

    for i in range(10):
        result = executor.submit(square, i)  # 1st arg is function, rest are args to it
        all_results.append(result)

    print(all_results)
