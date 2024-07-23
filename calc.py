#!/usr/bin/env python3

def add(x:float, y:float) -> float:
    return x + y

def sub(x:float, y:float) -> float:
    return x - y

ops = {'+':add,
       '-':sub}

while s := input('Enter math expression: ').strip():
    first, op, second = s.split()

    try:
        first_n = int(first)
        second_n = int(second)

        if op in ops:
            result = ops[op](first_n, second_n)
        else:
            result = f'Bad operator {op}'

        print(f'{first} {op} {second} = {result}')

    except ValueError as e:
        print(f'Try again: {e}')
