#!/usr/bin/env python3
import math

def isprime(num) :
    for i in range(2, int(math.sqrt(num) + 1)) :
        if num % i == 0 :
            return False
        return True

yes_or_no = list()

for i in range(int(input())) :
    num = int(input())
    if isprime(num) :
        yes_or_no.append("yes")
    else :
        yes_or_no.append("no")

for x in yes_or_no :
    print(x)
