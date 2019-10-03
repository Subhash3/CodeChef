#!/usr/bin/env python3

import math

for i in range(int(input())) :
    (A, B) = map(int, input().split())
    b = -2*(A + B)
    a = 3
    c = A*B
    discriminant = (b**2) - 4*(a*c)

    x = -b - math.sqrt(discriminant)
    x /= 2*a
#    x = math.ceil(x)
    volume = x * (x-A) * (x-B)
    print(x, volume)
