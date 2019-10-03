#!/usr/bin/python3

MODULO = 1000000007

# def f(x) :
#     fx = 0
#     e = 0
#     while x > 0 :
#         d = x%10
#         while x > 0 :
#             x = int(x/10)
#             last_digit = x%10
#             if d == last_digit :
#                 e += 1
#             else :
#                 break
#         k = d*(10**e)
#         fx =  (fx%MODULO  + k%MODULO)%MODULO
#         # print("\tf(x):", fx)
#         d = last_digit
#         e += 1
#     return fx

def f(x) :
    fx = 0
    n = len(x)
    i = 0
    while i < n :
        e = n-(i+1)
        digit = x[i]
        i += 1
        while i < n :
            if x[i] == digit :
                i += 1
            else :
                break
        fx = (fx%MODULO + (int(digit)*10**e)%MODULO)%MODULO
    return fx

def get_password(Nl, L, Nr, R) :
    password = 0
    left = int(L)
    right = int(R)

    for x in range(left, right+1) :
        x = str(x)
        # print("x:", x)
        password = (password%MODULO + f(x))%MODULO
        # print(password)
    # print("Final:", password)
    return password%MODULO

try :
    T = int(input())
except :
    quit()

for test_case in range(T) :
    Nl, L = map(int, input().split())
    Nr, R = map(int, input().split())    
    password = get_password(Nl, L, Nr, R)
    print(password)
