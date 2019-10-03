#!/usr/bin/python3

import random

correct = ""
N = int(input())
for i in range(N) :
    a = random.randint(1, 5)
    if a == 1 :
        correct += 'A'
    elif a == 2 :
        correct += 'B'
    elif a == 3 :
        correct += 'C'
    else :
        correct += 'D'

chef = ""
for i in range(N) :
    a = random.randint(1, 6)
    if a == 1 :
        chef += 'A'
    elif a == 2 :
        chef+= 'B'
    elif a == 3 :
        chef += 'C'
    elif a == 4 :
        chef += 'D'
    else :
        chef += 'N'
print(int(1))
print(N)
print(correct)
print(chef)
