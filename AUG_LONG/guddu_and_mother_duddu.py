#!/usr/bin/python3

def prefix_xors(A, N) :
    xors = dict()
    # common_xors = dict()
    val = A[0]
    count = 0
    for i in range(N) :
        if i == 0 :
            xors[val] = [[i], 0, 1]
            if A[i] == 0 :
                count += i
        else :
            val ^= A[i]
            if val == 0:
                count += i
            if val in xors :
                xors[val][0].append(i)
                xors[val][2] += 1
                l = xors[val][2]
                # print(xors[val])
                # print(val, ":", i, "-",  xors[val][0][l-2], "+1")
                xors[val][1] += i - xors[val][0][l-2] +1
            else :
                xors[val] = [[i], 0, 1]
    
    for element in xors.values() :
        count += element[1]

    return xors, count

try :
    T = int(input())
except :
    quit()

for test_case in range(T) :
    N = int(input())
    A = list(map(int, input().split()))
    print(prefix_xors(A, N))