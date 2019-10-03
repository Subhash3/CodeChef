#!/usr/bin/python3

# def xor(A, i, j, k) :
#     value1 = A[i]
#     for x in range(i+1, j) :
#         value1 = value1 ^ A[x]
#     value2 = A[j]
#     for y in range(j+1, k+1) :
#         value2 = value2 ^ A[y]

#     return value1 == value2

# def xor(A, i, j, k) :
#     v1 = A[i]
#     v2 = A[j]

#     x = i +1
#     y = j+1

#     flag1 = flag2 = False
#     while True :
#         if flag1 and flag2 :
#             break
#         if x < j :
#             v1 = v1 ^ A[x]
#             x += 1
#         else :
#             flag1 = True
        
#         if y < k+1 :
#             v2 = v2 ^ A[y]
#             y += 1
#         else :
#             flag2 = True
            
#     return v1 == v2

def get_triads(A, N) :
    count = 0
    val = 0
    for i in range(N) :
        for j in range(i+1, N) :
            val ^= A[j]
            if A[i] == val :
                count += j-i

    return count

try :
    T = int(input())
except :
    quit()

for test_case in range(T) :
    N = int(input())
    A = list(map(int, input().split()))
    ans = get_triads(A, N)
    print(ans)
