#!/usr/bin/python3

try :
    T = int(input())
except :
    quit()

for test_case in range(T) :
    values = list(map(int, input().split()))
    N = int(values[0])
    M = int(values[1])

   
    print(N*M, end=' ')
    for K in range(2, N*M+1-3) :
        first_hero = set()
        second_hero = set()
        S = set()
        common = 0
        cells = 0
        i1 = j1 = 0
        i2 = j2 = 0
        # print("K:", K)
        while True :
            if cells >= N*M:
                break
            i1 = cells // M
            j1 = cells % M

            i2 = cells % N
            j2 = cells // N
            # print("cells: ", cells, "(i1, j1): ", i1, j1, "(i2, j2): ", i2, j2)

            S.add((i1, j1))
            S.add((i2, j2))

            cells += K
        print(len(S), end=' ')
    print(3, 2, 1)
