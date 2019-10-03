#!/usr/bin/python3

def xor_list(lst) :
    value = 0
    # print(lst)
    for i in lst :
        value ^= int(i)
    # print(value)
    return value

def max_peace_val(lst, K, N) :
    xor_peace_vals = list()
    start = 0
    end = K
    while end <= N :
        segment = lst[start: end]
        xor_val = xor_list(segment)
        xor_peace_vals.append(xor_val)
        start += 1
        end += 1

    return max(xor_peace_vals)

try:
    test_cases = int(input())
except :
    quit()

for case in range(test_cases) :
    N, K = input().split()
    peaceValues = input().split()
    print(max_peace_val(peaceValues, int(K), int(N)))