#!/usr/bin/env python3

from typing import Sequence, Union

def mysum(*numbers)
    total : float = 0

    for one_number in numbers:
        total += one_number

    return total

print(mysum(10, 20, 30, 40, 50))
print(mysum(10, 20, 30, 40.0, 50))
