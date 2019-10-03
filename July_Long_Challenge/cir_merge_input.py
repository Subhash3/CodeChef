#!/usr/bin/python3

import random

print(1)
N = int(input())
print(N)
for i in range(N) :
    num = random.randint(1, 10000)
    print(num, end=' ')
print()
