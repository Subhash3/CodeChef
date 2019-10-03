#!/usr/bin/env python3
import math

def prime_count(number) :
    primes = list()
    pcount = 0
    fcount = 0
    num = 2
    while num <= number :
        for i in range(2, int(math.sqrt(num)) + 1) :
            if num % i == 0 :
                fcount += 1
                break
        if fcount == 0 :
            primes.append(num)
        fcount = 0
        num += 1
    count = 0
    print(primes)
    for p in primes :
        if number % p == 0 :
            count += 1
    return count

energy = list()
for i in range(int(input())) :
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    count = 0
    for num in range(n, m) :
        count += prime_count(num)
    energy.append(count)
for e in energy :
    print(e)
