#!/usr/bin/python3

def isJosh(i, Arr) :
    if Arr[i] == 'D' :
        return True
    return False

def get_week_soliders(Arr, N, F) :
    week_soliders = set()
    num_week_soliders = 0
    for solider in Arr :
        if solider == 'D' :
            pass
        elif solider <= F :
            week_soliders.add(solider)
            num_week_soliders += 1
    return week_soliders, num_week_soliders

try :
    T = int(input())
except :
    quit()

for test_case in range(T) :
    N = int(input())
    Arr = list(map(int, input().split()))
    F = int(input())

    # if min(Arr) > F :
    #     print("impossible")
    #     continue

    alive = N
    minimum_possible = dict()
    for p in range(N-1) :
        josh_pos = p
        hits = 0
        # possible = True
        D = 0
        temp = list(Arr)
        Arr.insert(josh_pos, 'D')
        solider_next_to_josh = (josh_pos+1)%N # he never dies since josh doesn't hit him
        if Arr[solider_next_to_josh] <= F :
            attacker = 0
            week_soliders, num_week_soliders = get_week_soliders(Arr, N, F)
            while alive > 2 :
                if num_week_soliders <= 0 :
                    alive = 0
                    break
                # print(Arr, "Now the Attacker is :", attacker, Arr[attacker])
                if isJosh(attacker, Arr) :
                    attacker = (attacker+1)%alive
                    # print("Josh doesn't do anythings and gives the sword to", Arr[attacker])
                    continue
                defender = (attacker+1)%alive
                if isJosh(defender, Arr) :
                    hits += 1
                    D += Arr[attacker]
                    # print(Arr[attacker], "Hits Josh and gives him the sword. Josh's power: ", D)
                    attacker = (attacker +1)%alive
                else :
                    if defender in week_soliders :
                        week_soliders.remove(defender)
                        # print("Defender is one of the week soliders")
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
                    else :
                        possible = True

            # print(Arr)
            Arr = temp
            alive = N
            if possible :
                # print("Position ", josh_pos+1, "is safe")
                # print(josh_pos+1, D)
                if minimum_possible == {} or D < minimum_possible["D"] :
                    minimum_possible["D"] = D
                    minimum_possible["P"] = josh_pos+1
            # print("-----------\nJosh got hit", hits, "times\n-------------\n")
        Arr = temp
    if minimum_possible == {} :
        print("impossible")
    else :
        print("possible")
        print(minimum_possible["P"], minimum_possible["D"])
            # break
        # input()