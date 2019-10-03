#!/usr/bin/env python3
for i in range(int(input())):
    N, K = map(int, input().split())
    if N < K:
        print(N)
    else:
        m = 0
        while K > m + 1:
            if (N % K) > m:
                m = N % K
            K -= 1
        print(m) 
