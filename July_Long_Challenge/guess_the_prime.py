#!/usr/bin/python3

import random
import math

def isInt(p) :
    k = int(p)
    if p-k != 0 :
        return False
    return True

def isPrime(p) :
    for i in range(2, int(math.sqrt(p))+1) :
        if p % i == 0 :
            return False
    return True


try :
    T = int(input())
except :
    quit()

for test_case in range(T) :
    # x = int(input())
    found = "no"
    while found != "yes" : 
        x = random.randint(1, 100)
        print(1, x)
        ans = int(input())
        if ans == -1 :
            quit()
        num = (x**2) - ans
        print(num)
        possible_primes = set()
        for k in range(2, num) :
            p = num/k
            if isInt(p) and isPrime(p):
                print(int(p))
                possible_primes.add(p)
        print("Possible primes:", possible_primes)
        if possible_primes == set() :
            print("Found:", num)
        found = input()

    