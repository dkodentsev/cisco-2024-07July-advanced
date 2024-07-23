#!/usr/bin/env python3

def mysum(numbers:list[float]) -> float:
    total : float = 0

    for one_number in numbers:
        total += one_number

    return total

print(mysum([10, 20, 30, 40, 50]))
print(mysum([10, 20, 30, 40.0, 50]))
print(mysum({10, 20, 30, 40.0, 50}))
