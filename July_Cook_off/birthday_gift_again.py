#!/usr/bin/python3

def get_counts(U, length) :
    count_0 = 0
    count_1 = 0
    for i in range(length) :
        if U[i] == '0' :
            count_0 += 1
        else :
            count_1 += 1
    return count_0, count_1

def beauty(S, N) :
    b = 0
    for i in range(N) :
        num = 1
        count_0 = 0
        count_1 = 0
        start = i
        while True :
            length = num + num**2
            j = length+i
            if j > N :
                break
            U = S[start:j]
            print("U:", U, j-start)
            c0, c1 = get_counts(U, j-start)
            count_0 += c0
            count_1 += c1
            if count_0 == count_1**count_1 :
                print(S[i:j]," is special")
                b += 1
            start = length
            num += 1
    return b

try :
    T = int(input())
except :
    quit()

for test_case in range(T) :
    S = input()
    N = len(S)
    print(beauty(S, N))
