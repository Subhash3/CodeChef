#!/usr/bin/python3

MODULO = 1000000007

try :
    T = int(input())
except :
    quit()

for testCase in range(T) :
    N = int(input())
    fact = 1
    fact_fact = 1
    for i in range(1, N+1) :
        fact = (fact%MODULO * i%MODULO)
        fact_fact = (fact_fact%MODULO * fact%MODULO)%MODULO
    # print(i, "!: ", fact, fact, "!: ", fact_fact, sep=' ')
    print(fact_fact)