#!/usr/bin/python3

def sum_of_digits(num) :
    s = 0
    while num != 0 :
        s += (num)%10
        num = int(num/10)

    return s

def max_sum_product(Arr, N) :
    max_sum = 0
    for i in range(N) :
        for j in range(i+1, N) :
            prod = Arr[i]*Arr[j]
            s = sum_of_digits(prod)
            if s > max_sum :
                max_sum = s
    return max_sum

try :
    T = int(input())
except :
    quit()

for test_case in range(T) :
    N = int(input())
    Arr = list(map(int, input().split()))
    print(max_sum_product(Arr, N))
