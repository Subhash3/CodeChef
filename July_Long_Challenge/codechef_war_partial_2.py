#!/usr/bin/python3

import random

def isJosh(i, Arr) :
    if Arr[i] == 'D' :
        return True
    return False


try :
    T = int(input())
except :
    quit()

for test_case in range(1) :
    # N = int(input())
    # Arr = list(map(int, input().split()))
    # F = int(input())
    F = 10

    # if min(Arr) > F :
    #     print("impossible")
    #     continue
    for N in range(2, T) :
        Arr = list()
        for i in range(N-1) :
            Arr.append(random.randint(1, 100))
        alive = N
        minimum_possible = dict()
        print("N:", N)
        for josh_pos in range(N) :
            # if Arr[(josh_pos+1)%alive] > F :
            #     continue
            hits = 0
            possible = True
            D = 0
            temp = list(Arr)
            Arr.insert(josh_pos, 'D')
            attacker = 0
            soliders_hit_josh = list()
            while alive > 2 :
                # print(Arr, "Now the Attacker is :", attacker, Arr[attacker])
                if isJosh(attacker, Arr) :
                    attacker = (attacker+1)%alive
                    # print("Josh doesn't do anythings and gives the sword to", Arr[attacker])
                    continue
                defender = (attacker+1)%alive
                if isJosh(defender, Arr) :
                    soliders_hit_josh.append(attacker)
                    hits += 1
                    D += Arr[attacker]
                    # print(Arr[attacker], "Hits Josh and gives him the sword. Josh's power: ", D)
                    attacker = (attacker +1)%alive
                else :
                    # print(Arr[attacker], "Kills", Arr[defender], end=" ")
                    if defender == alive -1 : # last_guy
                        attacker = 0
                    elif defender == 0 : # first guy
                        attacker = 0
                    else :
                        attacker = (attacker +1)%(alive-1)
                    Arr.pop(defender)
                    alive -= 1
                    # print("And gives the sword to", Arr[attacker])
            # print("Only two guys are left, and bitland attacks them with: ", F)
            for solider in range(alive) :
                if isJosh(solider, Arr) :
                    D += F
                else :
                    Arr[solider] -= F
                    if Arr[solider] > 0 :
                        possible = False
                        # print("The other bitland solider is still alive. Josh dies.")
                        # print("Position:", josh_pos, " is not safe")
            # print(Arr)
            Arr = temp
            alive = N
            if possible :
                # print("Position ", josh_pos+1, "is safe")
                # print(josh_pos+1, D)
                if minimum_possible == {} or D < minimum_possible["D"] :
                    minimum_possible["D"] = D
                    minimum_possible["P"] = josh_pos+1
            # print("-----------\nJosh got hit", hits, "times by", soliders_hit_josh, "\n-------------")
            print("\tPosition:", josh_pos, "Hits:", hits, "Hit by:", soliders_hit_josh)
        # if minimum_possible == {} :
        #     print("impossible")
        # else :
        #     print("possible")
        #     print(minimum_possible["P"], minimum_possible["D"])
                # break
            # input()