#!/usr/bin/python3

def remove_all(arr, val) :
    new_arr = list()
    for i in arr :
        if i != val :
            new_arr.append(i)
    return new_arr

def start_game(arr) :
    cherry = 0
    haz = 0
    turn = 1 # cherry's turn
    while arr != [] and arr.count(0) != len(arr) :
        num = max(arr)
        if arr.count(num) > 1 :
            arr = remove_all(arr, num)
            score = 0
        else :
            score = arr.pop(arr.index(num))
            arr.append(int(score/2))
        # print(cherry, haz, arr)
        # input()
        if turn == 1 :
            cherry += score
            turn = 0
        elif turn == 0 :
            haz += score
            turn = 1
    if cherry > haz :
        return "Cherry " + str(cherry)
    else :
        return "Hazardous"

try:
    t = int(input())
except :
    quit()

for case in range(t) :
    N = int(input())
    vals = input().split()
    arr = [int(i) for i in vals]
    winner = start_game(arr)
    print(winner)