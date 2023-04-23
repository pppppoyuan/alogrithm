# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random
import time

# Linear search algorithm
def linear_search(S, x):
    for i in range(len(S)):
        if S[i] == x:
            return True
    return False

# Binary search algorithm
def binary_search(S, x):
    low = 0
    high = len(S) - 1
    while low <= high:
        mid = (low + high) // 2
        if S[mid] == x:
            return True
        elif S[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return False

# Fibonacci search algorithm
def fibonacci_search(S, x):
    def fib(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fib(n-1) + fib(n-2)
    n = len(S)
    k = 0
    while fib(k) < n:
        k += 1
    offset = -1
    while fib(k) > 1:
        i = min(offset + fib(k-2), n-1)
        if S[i] < x:
            k -= 1
            offset = i
        elif S[i] > x:
            k -= 2
        else:
            return True
    if fib(k-1) and S[offset+1] == x:
        return True
    return False

# Generate random list S and integer x
S = random.sample(range(1000000), 10)
x = random.randint(0, 999999)

# Measure execution times for different list sizes
for n in range(10, 1010, 10):
    total_time_linear = 0
    total_time_binary = 0
    total_time_fibonacci = 0
    for i in range(5):
        S = random.sample(range(1000000), n)
        start_time = time.time()
        linear_search(S, x)
        end_time = time.time()
        total_time_linear += end_time - start_time
        start_time = time.time()
        binary_search(S, x)
        end_time = time.time()
        total_time_binary += end_time - start_time
        start_time = time.time()
        fibonacci_search(S, x)
        end_time = time.time()
        total_time_fibonacci += end_time - start_time
    print("n =", n, " Linear search time:", total_time_linear/5, " Binary search time:", total_time_binary/5, " Fibonacci search time:", total_time_fibonacci/5)
