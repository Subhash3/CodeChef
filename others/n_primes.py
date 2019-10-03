#!/usr/bin/env python3
import math

primes = list()
#pcount = 0
fcount = 0
num = 2
#N = 1000000
number = 10**6

#while pcount < N :
while num <= number :
    for i in range(2, int(math.sqrt(num))) :
        if num % i == 0 :
            fcount += 1
            break
    if fcount == 0 :
        primes.append(num)
        #pcount += 1
    fcount = 0
    num += 1

print(primes)
