#!/usr/bin/python3

import math

def max_moves(Xf) :
    X = 0
    Y = 0
    moves = 0
    while X < Xf :
        P = int(math.sqrt(Y)) +1
        X = P
        if X > Xf :
            break
        Y += P**2
        moves += 1
    return moves

try :
    T = int(input())
except :
    quit()

for test_case in range(T) :
    Xf = int(input())
    print(max_moves(Xf))
