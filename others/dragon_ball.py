#!/usr/bin/env python3
import math
import statistics

ans = list()
for i in range(int(input())) :
    nq = input().split()
    N = int(nq[0])
    Q = int(nq[1])
    integers = input().split()
    for i in range(N) :
        integers[i] = int(integers[i])
    for i in range(Q) :
        queries = input().split()
        if int(queries[0]) == 1 :
            L = int(queries[1])
            R = int(queries[2])
            mo = mayh.floor(statistics.mode(integers[L-1:R]))
            me = statistics.median(integers[L-1:R])
            l = math.lcm(mo, me)
            ans.append(l)
            #ans.append(math.lcm(statistics.mode(integers[L-1:R]), statistics.median(L-1:R)))
        elif int(queries[0] == 2) :
            i = int(queries[1])
            x = int(queries[2])
            integers[i-1] = x
for a in ans :
    print(a)
