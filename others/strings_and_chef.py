#!/usr/bin/env python3

strings = list()
counts = list()

for i in range(int(input())) :
    strings.append(input())
Q = int(input())
for i in range(Q) :
    queires = input().split()
    L = int(queires[0])
    R = int(queires[1])
    C = int(queires[2])
    P = queires[3]

    count = 0
    for string in strings[L-1:R] :
        try :
            if string[C-1] == P :
                count += 1
        except :
            continue
    counts.append(count)
for count in counts :
    print(count)
