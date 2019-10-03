#!/usr/bin/env python3
import math

for i in range(int(input())) :
    nums = input().split()
    a = int(nums[0])
    b = int(nums[1])
    g = math.gcd(a, b)
    l = int((a * b)/g)
    print(g, l)
