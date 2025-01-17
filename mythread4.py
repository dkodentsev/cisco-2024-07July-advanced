#!/usr/bin/env python3

# I want to run a function numerous times concurrently with itself.
# I can do that with threads:
# - I define the function
# - I start up a bunch of threads, telling them to execute that function
# - I tell the threads to run

import time
import random
import threading

l = threading.Lock()  # create a new lock object

def hello(n):
    time.sleep(random.randint(0, 3))

    with l:
        print(f'[{n}] Hello!')
        print(f'[{n}] Hello again!')

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
