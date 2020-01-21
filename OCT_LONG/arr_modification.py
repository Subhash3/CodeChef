#!/usr/bin/python3

try :
    T = int(input())
except :
    quit()

for testCase in range(T) :
    N, K = map(int, input().split())
    Arr = list(map(int, input().split()))

    possible_values = list()

    for i in range(N) :
        a = Arr[i]
        b = Arr[N-(i%N)-1]
        if i < int(N/2) :
            possible_values.append((a^b, b, a))
        else :
            possible_values.append((b, a^b, a))

    # print(possible_values)

    a = list()
    for i in range(N) :
        r = (K -i -1)//N
        r = r%3
        # print("r: ", r, end=" ")
        a.append(possible_values[i][r])
    if N%2 == 1 and K > N//2 :
        a[N//2] = 0
    for num in a :
        print(num, end = " ")
    print()
