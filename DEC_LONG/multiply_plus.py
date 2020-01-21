#!/usr/bin/python3

def c(n, k): 
    C = [[0 for x in range(k+1)] for x in range(n+1)] 
  
    for i in range(n+1): 
        for j in range(min(i, k)+1): 
            if j == 0 or j == i: 
                C[i][j] = 1  
            else: 
                C[i][j] = C[i-1][j-1] + C[i-1][j] 
  
    return C[n][k] 

try :
    T = int(input())
except :
    quit()

for testCase in range(T) :
    N = int(input())
    arr = list(map(int, input().split()))
    zeros = 0
    twos = 0
    for i in range(N) :
        if arr[i] == 0 :
            zeros += 1
        elif arr[i] == 2 :
            twos += 1
    count = 0
    if zeros > 1 :
        count += c(zeros, 2)
    if twos > 1 :
        count += c(twos, 2)

    print(count)

# def f(N) :
#     for i in range(N) :
#         for j in range(N) :
#             # print(i, j, i+j, i*j)
#             if i+j == i*j :
#                 print(i, j)
#     return

# N = int(input())
# f(N)