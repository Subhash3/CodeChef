#!/usr/bin/env python3
i = 0
ans = 0

for i in range(int(input())) :
    B = int(int(input())/2)
    for j in range(B) :
        ans += i
        i += 1
    print(ans)
    ans = 0
    i = 0
