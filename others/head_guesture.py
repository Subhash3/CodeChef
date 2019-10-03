#!/usr/bin/env python3
for i in range(int(input())) :
    N = int(input())
    guestures = input()
    if 'I' in guestures :
        print('INDIAN')
    elif 'Y' in guestures :
        print('NOT INDIAN')
    else :
        print('NOT SURE')
