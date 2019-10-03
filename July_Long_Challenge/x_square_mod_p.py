#!/usr/bin/python3

import math

def f(x, p) :
    print("X:", x, "P:", p, "\tAns:", (x**2)%p)
    return

def isPrime(p) :
    for i in range(2, int(math.sqrt(p))+1) :
        if p % i == 0 :
            return False
    return True

# p = int(input("Enter a prime: "))
for p in range(2, 100) :
    if isPrime(p) :
        for x in range(1, 2*p+1) :
            f(x, p)
        input()