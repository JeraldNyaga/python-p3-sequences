#!/usr/bin/env python3

def print_fibonacci(length):
    first = 0
    second = 1
    fibo = []

    if length == 1:
        fibo.append(first)
    elif length == 2:
        fibo.append(first)
        fibo.append(second)
    else:
        while len(fibo) < length:
            fibo.append(first)
            first = second
            second = second + fibo[-1]
    print(fibo)

