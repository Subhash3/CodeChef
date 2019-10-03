#!/usr/bin/python3

# def final_radiation(initial, C, N) :
#     for i in range(N) :
#         start = i+1 - C[i] -1
#         if start < 0 :
#             start = 0
#         end = i+1 + C[i]
#         if end >= N :
#             end = N
#         # print(start, end)
#         for j in range(start, end) :
#             initial[j] += 1
#     return initial

def final_radiation(initial, C, N) :
    S = 0
    E = N
    for i in range(N) :
        start = i+1 - C[i] -1
        if start < 0 :
            start = 0
        end = i+1 + C[i]
        if end >= N :
            end = N
        # print(start, end)
        for j in range(S, start) :
            initial[j] -= 1
        for j in range(end, E) :
            initial[j] -= 1
        # print(initial)
    return initial

# # Is zombies array a permutation of radiations array ?
# def is_arr_perm(radiations, zombies, N) :
#     Nz = N
#     for i in range(N) :
#         r = radiations[i]
#         flag = False
#         for j in range(Nz) :
#             if zombies[j] == r :
#                 zombies.pop(j)
#                 Nz -= 1
#                 flag = True
#                 break
#         if not flag :
#             return False
#     return True

def is_arr_perm(radiations, zombies, N) :
    radiations.sort()
    zombies.sort()
    for i in range(N) :
        if radiations[i] != zombies[i] :
            return False
    return True

try :
    T = int(input())
except :
    quit()

for test_case in range(T) :
    N = int(input())
    C = list(map(int, input().split()))
    Z = list(map(int, input().split()))
    radiations = [N]*N
    radiations = final_radiation(radiations, C, N)
    # print(radiations)
    if is_arr_perm(radiations, Z, N) :
        print("YES")
    else :
        print("NO")
