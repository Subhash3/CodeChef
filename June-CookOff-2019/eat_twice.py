#!/usr/bin/python3

def get_max_taste(N, days, tastes) :
    days_and_max_tastes = dict()
    for i in range(N) :
        if days[i] not in days_and_max_tastes :
            days_and_max_tastes[days[i]] = tastes[i]
        else :
            if tastes[i] > days_and_max_tastes[days[i]] :
                days_and_max_tastes[days[i]] = tastes[i]

    max_tastes = sorted(days_and_max_tastes.values())
    return max_tastes[-1] + max_tastes[-2]


try :
    T = int(input())
except :
    quit()

for test_case in range(T) :
    N_M = input().split()
    N = int(N_M[0])
    M = int(N_M[1])
    days = list()
    tastes = list()
    for i in range(N) :
        days_tastes = input().split()
        days.append(int(days_tastes[0]))
        tastes.append(int(days_tastes[1]))
    maxTaste = get_max_taste(N, days, tastes)
    print(maxTaste)
