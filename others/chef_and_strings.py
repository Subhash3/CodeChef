#!/usr/bin/env python3
for i in range(int(input())) :
    s1 = input()
    s2 = input()
    minimal = 0
    maximal = 0
    for l in range(len(s1)) :
        if s1[l] == '?' or s2[l] == '?':
            maximal += 1
            continue
        if s1[l] != s2[l] :
            minimal += 1
            maximal += 1
            continue
    print(minimal, maximal)
