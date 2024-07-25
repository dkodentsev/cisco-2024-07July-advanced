#!/usr/bin/env python3

# I want to run a function numerous times concurrently with itself.
# I can do that with threads:
# - I define the function
# - I start up a bunch of threads, telling them to execute that function
# - I tell the threads to run

# a queue object is kind of like a list, but it's guaranteed to be thread safe
# we use the put method to add something to the end, and the get method to
# retrieve from the beginning (FIFO, first in, first out)

import time
import random
import threading
import queue

l = threading.Lock()  # create a new lock object
q = queue.Queue()     # create a queue onto which functions can put output

def hello(n):
    time.sleep(random.randint(0, 3))

    with l:
        q.put(f'[{n}] Hello!')
        q.put(f'[{n}] Hello again!')

for i in range(10):
    # create a new Thread object, telling it what function to run
    # whatever arguments we want to pass are in the "args" kwargs
    t = threading.Thread(target=hello, args=(i,))
    t.start()

# join them together, meaning: wait for all of them to finish
# have a while loop wait until the number of threads is down to 1
while threading.active_count() > 1:
    for one_thread in threading.enumerate():
        if one_thread == threading.current_thread():
            continue
        one_thread.join(0.01)  # normally, join blocks

print('Done!')
