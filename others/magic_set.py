#!/usr/bin/env python3

def sub_seq(seq, n, m) :
    good_seq_count = 0
    for i in range(n) :
        for j in range(i, n) :
            sub = list()
            for k in range(i, j+1) :
                sub.append(seq[k])
            if sum(sub) % m == 0 :
                good_seq_count += 1
    return good_seq_count



for test_case in range(int(input())) :
    n_and_m = input().split()
    n = int(n_and_m[0])
    m = int(n_and_m[1])
    integers = list(map(int, input().split()))
    ans = sub_seq(integers, n, m)
    if sum(integers) % m == 0 :
        ans -= 1
    print(ans)


