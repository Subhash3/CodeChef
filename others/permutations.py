#!/usr/bin/env python3
import math

for i in range(int(input())) :
    n_k = input().split()
    n = int(n_k[0])
    k = int(n_k[1])
    integers = input().split()
    integers = list(map(int, integers))
    r = integers.count(0)
    a = math.factorial(r)
    print(a)
