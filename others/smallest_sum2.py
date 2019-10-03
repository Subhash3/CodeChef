#!/usr/bin/env python3
sums = list()
for i in range(int(input())) :
    N = int(input())
    integers = list(map(int, input().split()))
    integers.sort()
    print(integers[0] + integers[1])
