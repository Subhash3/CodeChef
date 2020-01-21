#!/usr/bin/python3

try :
    T = int(input())
except :
    quit()

for test_case in range(T) :
    N, M, q = map(int, input().split())
    flag = False

    columnar_matrix = list()
    for i in range(N) :
        columnar_matrix.append(False)
    row_matrix = list()
    for j in range(M) :
        row_matrix.append(False)

    print("Done!")
    # print(row_matrix)
    # print(columnar_matrix)

    for query in range(q) :
        x, y = map(int, input().split())
        if q == 1 :
            flag = True
            break
        columnar_matrix[x-1] = not (columnar_matrix[x-1])
        row_matrix[y-1] = not (row_matrix[y-1])

    if flag :
        print(M +N -2)
    else :
        count = 0
        for a in columnar_matrix :
            for b in row_matrix :
                if a^b :
                    count += 1
        print(count)