#!/usr/bin/env python3
for i in range(int(input())) :
    angles = [int(x) for x in input().split()]
    if sum(angles) == 180 :
        print("YES")
    else :
        print("NO")
