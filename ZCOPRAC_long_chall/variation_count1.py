#!/usr/bin/python3

def get_variation_count_ef(vals, K, N) :
    vals.sort()
    count = 0
    for i in range(N) :
        for j in range(i+1, N) :
            if abs(vals[i]-vals[j]) >= K :
                count += N-j
                break
    return count


try :
    N, K = input().split()
except :
    quit()
N = int(N)
K = int(K)
values = list(map(int, input().split()))
print(get_variation_count_ef(values, K, N))
