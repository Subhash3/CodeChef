#!/usr/bin/python3

def kill(Arr, n, p, hits, D) :
    first = Arr[:p]
    second = Arr[p+1:]
    if first == None or first == [] :
        i = 0
        while True :
            try :
                second[2*i +1] = 0
            except :
                break
            i += 1
        second.insert(0, 'D')
        if second[-1] != 0 :
            hits.append(second[-1])
            D += second[-1]

        return second, hits
    
    if second == None or second == [] :
        i = 0
        while True :
            try :
                first[2*i +1] = 0
            except :
                break
            i += 1
        if first[-1] != 0 :
            hits.append(first[-1])
            D += first[-1]
        first.append('D')        
        return first, hits

    i = 0
    # print(first)
    while True :
        try :
            first[2*i +1] = 0
        except :
            break
        i += 1
    first.append('D')
    # print(first)
    i = 0
    # print(second)
    while True :
        try :
            second[2*i +1] = 0
        except :
            break
        i += 1
    # print(second)

    new = first + second
    if new[-1] != 0 and new[-1] != 'D' :
        new[0] = 0
    return new, hits

def remove_all_k(Arr, n, k) :
    new = list()
    count = 0
    killed = 0
    p = None
    for i in range(n) :
        num = Arr[i]
        if num == 'D' :
            new.append('D')
            p = count
            count += 1
        elif num == k :
            killed += 1
        else :
            new.append(num)
            count += 1
    return new, killed, p

try :
    T = int(input())
except :
    quit()

for test_case in range(T) :
    N = int(input())
    Arr = list(map(int, input().split()))
    F = int(input())

    alive = N
    min_D = P = None
    for josh_pos in range(N) :
        temp = list(Arr)
        Arr.insert(josh_pos, 'D')
        # print(Arr)
        hits = list()
        p = josh_pos
        D = 0
        while alive > 2 :
            if p % 2 == 1 :
                hits.append(Arr[p-1])
                D += Arr[p-1]
            Arr, hits = kill(Arr, alive, p, hits, D)
            # print("After killing:", Arr)
            Arr, killed, p = remove_all_k(Arr, alive, 0)
            # print("After removing:", Arr, "Josh is at:", p)
            alive -= killed
        # print("Josh was hit by:", hits)
        # print("Under bitland's", F, "Attack", Arr)
        for solider in Arr :
            if solider == 'D' :
                D += F
            else :
                solider -= F
                if solider > 0 :
                    possible = False
                else :
                    possible = True
        if possible :
            if min_D == None or D < min_D :
                min_D = D
                P = josh_pos
        else :
            pass
                
        Arr = temp
        alive = N
        # print()

    # print("\n")
    if not min_D == None :
        print("possible")
        print(P+1, min_D)
    else :
        print("impossible")