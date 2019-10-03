#!/usr/bin/python3

def get_safe_houses_for_theif(x, y, houses) :
    to_be_secured = set(range(1, 101)) # set {1, 2....100}
    # print("Houses to be secured: ", to_be_secured)
    secured_so_far = set()
    for i in houses :
        # Cops at house[i] can secure from {From} to {To}.
        From = int(i) - x*y
        if From < 1 :
            From = 1
        To = int(i) + x*y
        if To > 100 :
            To = 100
        secured_so_far = secured_so_far.union(set(range(From, To+1)))
        # print("Houses Secured so far: ", secured_so_far)
        if to_be_secured.difference(secured_so_far) == set() :
            return 0 # All houses are secured
    return len(to_be_secured.difference(secured_so_far))

test_cases = int(input())
for case in range(test_cases) :
    M, x, y = input().split()
    houses = input().split()
    safe_houses = get_safe_houses_for_theif(int(x), int(y), houses)
    print(safe_houses)
