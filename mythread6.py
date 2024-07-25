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

def add(n):
    time.sleep(random.randint(0, 2))
    print('\tPutting {n**2}')
    q.put(n ** 2)

def get():
    while True:
        if q.empty():
            time.sleep(1)
        value = q.get()

        print(f'Got {value}')

        if value == 81:
            break


for i in range(10):
    t = threading.Thread(target=add, args=(i,))
    t.start()

threading.Thread(target=get).start()
