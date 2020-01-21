#!/usr/bin/python3

from math import ceil, sqrt

MAX_N = 1000001

smallest_prime_facts = list()

for i in range(MAX_N) :
    smallest_prime_facts.append(0)

def sieve(): 
    smallest_prime_facts[1] = 1
    for i in range(2, MAX_N): 
        if i >= 4 and i%2 == 0 :
            smallest_prime_facts[i] = 2
        else :
            smallest_prime_facts[i] = i

    # for i in range(4, MAX_N, 2): 
    # 	smallest_prime_facts[i] = 2

    for i in range(3, ceil(sqrt(MAX_N))): 	
        if (smallest_prime_facts[i] == i): 
            for j in range(i * i, MAX_N, i): 
                if (smallest_prime_facts[j] == j): 
                    smallest_prime_facts[j] = i 
def getFactorization(x): 
    prime_facts = set()
    while (x != 1): 
        prime_facts.add(smallest_prime_facts[x]) 
        x = x // smallest_prime_facts[x] 

    return prime_facts
sieve()

try :
    T = int(input())
except :
    quit()


for testCase in range(T) :
    N = int(input())

    prime_factors = dict()
    length = 0
    max_star = None
    max_value = None
    length = 0

    for n in input().split() :
        num = int(n)
        length += 1
        star = 0
        if num == 1:
            star = length-1
        else :
            x = num
            p = set()
            while x != 1 :
                prime = smallest_prime_facts[x]
                x = x // prime
                if prime not in p :
                    if prime not in prime_factors :
                        prime_factors[prime] = [{num}, 1]
                    else :
                        prime_factors[prime][0].add(num)
                        prime_factors[prime][1] += 1
                p.add(prime)
            # if num not in p :
            #     if num not in prime_factors :
            #         prime_factors[num] = [{num}, 1]
            #     else :
            #         prime_factors[num][0].add(num)
            #         prime_factors[num][1] += 1
            # star = prime_factors[num][1] -1
            print(num, prime_factors)

            common = set()
            count = 0
            x = num
            while x != 1 :
                p = set()
                prime = smallest_prime_facts[x]
                if prime not in p :
                    if x == num :
                        common = prime_factors[prime][0]
                    else :
                        common = common.intersection(prime_factors[prime][0])
                p.add(prime)
                x = x // prime

            # p.add(num)
            # common = common.intersection(prime_factors[num][0])
            star = len(common)
            # print(num, common, star)
        if max_star == None or max_star < star :
            max_star = star
    print(max_star)