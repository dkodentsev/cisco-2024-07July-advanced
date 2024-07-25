#!/usr/bin/env python3

# I want to run a function numerous times concurrently with itself.
# I can do that with threads:
# - I define the function
# - I start up a bunch of threads, telling them to execute that function
# - I tell the threads to run

import time
import random

def hello(n):
    time.sleep(random.randint(0, 3))
    print(f'[{n}] Hello!')
