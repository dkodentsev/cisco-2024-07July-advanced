#!/usr/bin/env python3

# I want to run a function numerous times concurrently with itself.
# I can do that with threads:
# - I define the function
# - I start up a bunch of threads, telling them to execute that function
# - I tell the threads to run

import time
import random
import threading

def hello(n):
    time.sleep(random.randint(0, 3))
    print(f'[{n}] Hello!')

all_threads = []

for i in range(10):
    # create a new Thread object, telling it what function to run
    # whatever arguments we want to pass are in the "args" kwargs
    t = threading.Thread(target=hello, args=(i,))
    t.start()
    all_threads.append(t)

# join them together, meaning: wait for all of them to finish
for one_thread in all_threads:
    one_thread.join()   # this blocks

print('Done!')
