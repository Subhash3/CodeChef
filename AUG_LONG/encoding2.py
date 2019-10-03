#!/usr/bin/python3

MODULO = 1000000007

def f(x) :
    # print("Number:", x)
    # if x < 10 :
    #     return [(x, 1, 0)], x
    # if x < 100 :
    #     remainder = x%11
    #     if remainder != 0 :
    #         return [], x
    #     else :
    #         return [], (x//10)*10


    pos = -1
    ans = 0
    digits_and_positions = list()
    while x > 0 :
        digit = x%10
        # print(digit, x)
        count = 0
        while x > 0 :
            k = x%10
            if k == digit :
                count += 1
                pos += 1
            else :
                digits_and_positions.append((digit, count, pos))
                val = digit*(10**pos)
                ans = (ans%MODULO + val%MODULO)%MODULO
                # print("digit:", digit, "count:", count, "position:", pos)
                # print("f(x):", ans, "val:", val)
                break
            x = x // 10
    digits_and_positions.append((digit, count, pos))
    val = digit*(10**pos)
    # print("digit:", digit, "count:", count, "position:", pos)
    # print("f(x):", ans, "val:", val)
    ans = (ans%MODULO + val%MODULO)%MODULO
    
    return digits_and_positions, ans


def get_password(Nl, L, Nr, R) :
    password = 0
    for x in range(L, R+1) :
        digits_and_positions, fx = f(x)
        # print(x, digits_and_positions, fx)
        password = (password%MODULO + fx%MODULO)%MODULO
        # print(x, fx)
    return password

try :
    T = int(input())
except :
    quit()

for test_case in range(T) :
    Nl, L = map(int, input().split())
    Nr, R = map(int, input().split())    
    password = get_password(Nl, L, Nr, R)
    print(password%MODULO)