#!/usr/bin/python3

try :
    T = int(input())
except :
    quit()

for test_case in range(T) :
    N, M, q = map(int, input().split())
    flag = False

    if q == 1 :
        flag = True
    else :
        columnar_matrix = list()
        row_matrix = list()


        # Create column and row matrices in the order of O(max(M, N))
        if N > M :
            for i in range(N) :
                if i < M :
                    row_matrix.append(False)
                columnar_matrix.append(False)
            
        else :
            for i in range(M) :
                if i < N :
                    columnar_matrix.append(False)
                row_matrix.append(False)     

    true_count_row_matrix = 0
    false_count_row_matrix = M
    for query in range(q) :
        x, y = map(int, input().split())
        if flag :
            break
        columnar_matrix[x-1] = not (columnar_matrix[x-1])
        row_matrix[y-1] = not (row_matrix[y-1])
        if row_matrix[y-1] :
            true_count_row_matrix += 1
        else :
            true_count_row_matrix -= 1

    if flag :
        print(M +N -2)
    else :
        print("Column Matrix", columnar_matrix)
        print("Row Matrix", row_matrix)
        false_count_row_matrix -= true_count_row_matrix
        print("False's", false_count_row_matrix)
        print("True's", true_count_row_matrix)
        count = 0
        for a in columnar_matrix :
            sub_count = 0
            if a :
                print("MM:", false_count_row_matrix)
            else :
                print("MM:", true_count_row_matrix)
            for b in row_matrix :
                if a^b :
                    count += 1
                    sub_count += 1
                    print("sub count", sub_count)
        print(count)