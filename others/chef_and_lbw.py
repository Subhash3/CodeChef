#!/usr/bin/python3

valid = [1, 0, 1, 1, 1]

for i in range(int(input())) :
    appeal = input().split()
    for j in range(len(appeal)) :
        appeal[j] = int(appeal[j])
    if appeal != valid :
        print('0')
    else :
        print('1')
