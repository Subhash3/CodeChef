#!/usr/bin/python3

def is_fair(n, values) :
    for i in range(n) :
        for j in range(i+1, n) :
            if values[i] < values[j] and values[i+n] >= values[j+n] :
                return "NOT FAIR"
            elif values[i] > values[j] and values[i+n] <= values[j+n] :
                return "NOT FAIR"
            elif values[i] == values[j] and values[i+n] != values[j+n] :
                return "NOT FAIR"
    return "FAIR"

try :
    T = int(input())
except :
    quit()

n = 3
for test_case in range(T) :
    values = list(map(int, input().split()))
    print(is_fair(n, values))
