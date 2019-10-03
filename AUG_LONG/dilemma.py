#!/usr/bin/python3

from time import sleep

def str_to_list(S) :
    l = list()
    i = 0
    zeroes = 0
    ones = 0
    while True :
        try :
            ch = S[i]
            l.append(ch)
            if ch == '0' :
                zeroes += 1
            else :
                ones += 1
        except :
            break
        i += 1

    return l, zeroes, ones

def flip(S, i, N) :
    S[i] = '9'
    if i -1 >= 0 :
        k = S[i-1]
        if k == '1' :
            S[i-1] = '0'
        elif k == '0' :
            S[i-1] = '1'
    if i + 1 < N :
        k = S[i+1]
        if k == '1' :
            S[i+1] = '0'
        elif k == '0' :
            S[i+1] = '1'
    return S


def game(S, N) :
    while True :
        removed = 0
        up = 0
        # down = 0
        if S[:2] == ['0', '9'] or S[-2:] == ['9', '0'] :
            return "LOSE"
        seen_a_nine = False
        seen_a_nine_zero = False
        seen_a_nine_zero_nine = False
        for i in range(N) :
            if seen_a_nine_zero_nine :
                return "LOSE"
            if S[i] == '1' :
                # print(S[i], " Card faced up. Removed it.")
                S = flip(S, i, N)
                # print("Flipped the adjacent cards:", S)
                up += 1
                seen_a_nine = False
                seen_a_nine_zero = False
                seen_a_nine_zero_nine = False
            elif S[i] == '9' :
                removed += 1
                if seen_a_nine_zero :
                    # print("Seen a 909")
                    seen_a_nine_zero_nine = True
                seen_a_nine = True
                # print("Seen a 9")
            else :
                if seen_a_nine :
                    # print("Seen a 90")
                    seen_a_nine_zero = True
                # print(S[i], " Card faced down. Do nothing")
                # down += 1
        if removed == N :
            return "WIN"
        # if up == 0 and down != 0 :
        if up == 0 :
            return "LOSE"

try :
    T = int(input())
except :
    quit()

for test_case in range(T) :
    S = input()
    # print("-------", S, "----------")
    S, zeroes, ones = str_to_list(S)
    N = zeroes + ones

    if ones%2 == 1 :
        print("WIN")
        continue
    if ones == 0 :
        print("LOSE")
        continue
    print(game(S, N))
