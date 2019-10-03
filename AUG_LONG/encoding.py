#!/usr/bin/python3

MODULO = 1000000007

def f(x) :
    pos = -1
    ans = 0
    # digits_and_positions = list()
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
                # digits_and_positions.append((digit, count, pos))
                val = digit*(10**pos)
                ans = (ans%MODULO + val%MODULO)%MODULO
                # print("digit:", digit, "count:", count, "position:", pos)
                # print("f(x):", ans, "val:", val)
                break
            x = x // 10
    # digits_and_positions.append((digit, count, pos))
    val = digit*(10**pos)
    # print("digit:", digit, "count:", count, "position:", pos)
    # print("f(x):", ans, "val:", val)
    ans = (ans%MODULO + val%MODULO)%MODULO
    
    # return digits_and_positions, ans
    return ans


def get_password(Nl, L, Nr, R) :
    password = 0
    x = L
    fx = f(x)
    first_digit = x%10
    second_digit = (x//10)%10
    if first_digit != second_digit :
        sum_without_first_digit = (fx%MODULO - first_digit%MODULO)%MODULO
    else :
        sum_without_first_digit = fx
    fx = 0
    while x < R +1 :
        print("sum without first digit:", sum_without_first_digit)
        first_digit = x%10
        second_digit = (x//10)%10
        if first_digit != second_digit :
            fx = x
        else :
            fx = sum_without_first_digit
        if first_digit == 9 :
            sum_without_first_digit += 10
        print(x, fx)

        password = (password%MODULO + fx%MODULO)%MODULO
        x += 1
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