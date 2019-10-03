#!/usr/bin/python3

MODULO = 1000000007

def get_coefficients(roots, n, coeff, K):     
    coeff[n] = 1
    for i in range(1, n + 1): 
        for j in range(n - i - 1, n):
            coeff[j] = (coeff[j] - (roots[i - 1] * coeff[j + 1]))

    return coeff

N, K = map(int, input().split())
Arr = dict()
no_of_roots = 0
coefficients = list()
for num in input().split() :
    num = int(num)
    if num in Arr :
        Arr[num] += 1
    else :
        Arr[num] = 1
        no_of_roots += 1
        coefficients.append(0)

coefficients.append(0)
# print(coefficients)
roots = list(Arr.values())
coefficients = get_coefficients(roots, no_of_roots, coefficients, K)
# print(coefficients)

s = 0
j = 0
for i in range(no_of_roots, -1, -1) :
    if j > K :
        break
    c = coefficients[i]
    if c < 0 :
        c = -c
    # print(c, s)
    s = (s%MODULO + c%MODULO)%MODULO
    j += 1

print(s)