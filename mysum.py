#!/usr/bin/env python3

def mysum(numbers:list[int]) -> int:
    total = 0

    for one_number in numbers:
        total += one_number

    return total

print(mysum([10, 20, 30, 40, 50]))
print(mysum([10, 20, 30, 'a', 50]))
