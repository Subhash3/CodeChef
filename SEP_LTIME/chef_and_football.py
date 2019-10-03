#!/usr/bin/python3

try :
    T = int(input())
except :
    quit()

for testCase in range(T) :
    predictable = False
    N = int(input())
    A = B = None
    for query in range(N) :
        choice, A_score, B_score = map(int, input().split())
        
        if choice == 1 :
            predictable = True
            A = A_score
            B = B_score
        else :
            if predictable :
                if A_score == B_score :
                    predictable = True
                    A = A_score
                    B = B_score
                else :
                    flag1 = flag2 = False
                    if A <= A_score and B <= B_score :
                        # print(A, "<=", A_score, "and", B, "<=", B_score)
                        flag1 = True
                        temp_A = A_score
                        temp_B = B_score
                        # print("Scores can be :", A_score, B_score)
                    if A <= B_score and B <= A_score :
                        # print(A, "<=", B_score, "and", B, "<=", A_score)
                        flag2 = True
                        temp_A = B_score
                        temp_B = A_score
                        # print("Scores can be :", B_score, A_score)
                    if flag1 ^ flag2 :
                        predictable = True
                        A = temp_A
                        B = temp_B
                    else :
                        predictable = False
                        A = B = None
            elif A_score == B_score :
                predictable = True
                A = A_score
                B = B_score
            else :
                predictable = False
                A = B = None

        if predictable :
            print("YES")
        else :
            print("NO")
        # print("Current scores: ", A, B)