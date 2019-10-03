#!/usr/bin/env python3
sums = list()
for i in range(int(input())) :
    N = int(input())
    integers = list(map(int, input().split()))
    #print(integers)
    #sums.append(min(integers)+min(integers.pop(min(integers))))
    min1 = min(integers)
    integers.pop(min1)
    min2 = min(integers)
    s = min1 + min2
    sums.append(s)
    integers = list()
for s in sums :
    print(s)
