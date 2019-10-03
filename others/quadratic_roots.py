#!/usr/bin/env python3

import math

A = int(input())
B = int(input())
C = int(input())

discriminant = (B*B) - (4*A*C)
if discriminant == 0 :
    x1 = (-B)/(2*A)
    x2 = (-B)/(2*A)
else :
    x1 = -B + math.sqrt(discriminant)
    x2 = -B - math.sqrt(discriminant)
    x1 /= 2*A
    x2 /= 2*A
print(x1)
print(x2)
