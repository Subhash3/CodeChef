#!/usr/bin/python3
import random

T = int(input())
print(T)
for i in range(T) :
    N = int(input())
    print(N)
    for j in range(N-1) :
        print(random.randint(1, 100000), end=" ")
    print()
    print(random.randint(1, 1000000))
