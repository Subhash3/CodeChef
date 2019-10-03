#!/usr/bin/env python3
for i in range(int(input())) :
    num = input()
    for j in range(len(num)) :
        if num[j] != num[-(j+1)] :
            print("losses")
            break
        if j == len(num) - 1 :
            print("wins")
