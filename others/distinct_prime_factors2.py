#!/usr/bin/env python3

import math

#Sieve of erastothenes
def sieve(n):
    numbers=range(0,n+1)
    for i in range(2,int(math.ceil(n**0.5))):
        if(numbers[i]):
            for j in range(i*i,n+1,i):
                numbers[j]=0
#removing 0 and 1 and returning a list
    numbers.remove(1)
    prime_numbers=set(numbers)
    prime_numbers.remove(0)

    primes=list(prime_numbers)
    primes.sort()
    return primes

    prime_numbers=[]
    prime_numbers=sieve(100000)
    #print prime_numbers
def no_of_distinct_prime_factors(n):
    count=0
    flag=0
    #print prime_numbers
    for i in prime_numbers:
            #print i
        if i>n:
            break
        if n%i==0:
            count+=1
            n=n/i
    return count

count = 0
for i in range(int(input())) :
    numbers = input().split()
    n = int(numbers[0])
    m = int(numbers[1])
    for i in range(n, m) :
        count += no_of_distinct_prime_factors(n)
print(count)
