#!/usr/bin/python3

# import time

# def get_variation_count(vals, K, N) :
#     count = 0
#     i = 0
#     while i < N :
#         j = i+1
#         while j < N :
#             if abs(vals[i] - vals[j]) >= K :
#                 count += 1
#             j += 1
#         i += 1
#     return count

# # A bit more efficient
def get_variation_count_ef(vals, K, N) :
    vals.sort()
    count = 0
    for i in range(N) :
        for j in range(i+1, N) :
            if abs(vals[i]-vals[j]) >= K :
                count += N-j
                break
    return count


N, K = input().split()
# start = time.time()
N = int(N)
K = int(K)
values = list(map(int, input().split()))
# print(values)
# print("Ans: ", get_variation_count(values, K, N))
# end = time.time()
# print(start-end)
# time.sleep(2)
# start = time.time()
print(get_variation_count_ef(values, K, N))
# end = time.time()
# print(start-end)
