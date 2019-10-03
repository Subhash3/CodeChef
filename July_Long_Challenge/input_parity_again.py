#!/usr/bin/python3

import time
import random

T = int(input())
print(T)
for t in range(T) :
    Q = random.randint(1, 100000)
    #Q = int(input())
    print(Q)
    for q in range(Q) :
        x = random.randint(1, 100000)
        print(x)
