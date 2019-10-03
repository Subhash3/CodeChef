#!/usr/bin/python3

def get_no_of_boxes(C) :

    A_cell = 0
    B_cell = N-1
    while True :
        if A_cell >= B_cell :
            # print(C)
            # print(A_cell, N-B_cell)
            return A_cell, N-B_cell
        # print(C)
        A_candies = C[A_cell]
        while A_candies <= X :
            C[A_cell] = 0
            A_cell += 1
            A_candies += C[A_cell]
            if A_cell >= B_cell :
                # print(C)
                # print(A_cell, N-B_cell)
                return A_cell, N-B_cell
        C[A_cell] -= X
        
        while C[B_cell] < 1 :
            if A_cell >= B_cell :
                # print(C)
                # print(A_cell, N-B_cell)
                return A_cell, N-B_cell
            B_cell -= 1
        C[B_cell] -= 1
    
    return A_cell, N-B_cell

try :
    T = int(input())
except :
    quit()

for testCase in range(T) :
    N = int(input())
    C = list(map(int, input().split()))
    X = int(input())
    ans = get_no_of_boxes(C)
    print(ans[0], ans[1])

