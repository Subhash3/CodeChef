#!/usr/bin/env python3

def get_min_difference(A, O, K) :
    for i in range(K) :
        # if apples are more, buy an apple
        if A > O :
            O += 1
        elif O > A : # if oranges are more, buy an orange
            A += 1
        else : # If both are of same quantity, needn't buy anything,
            # cuz, we want "minimum" possible difference
            break
    diff = A-O
    if diff < 0 :
        diff *= -1
    return diff

test_cases = int(input())
for case in range(test_cases) :
    A, O, K = input().split()
    min_diff = get_min_difference(int(A), int(O), int(K))
    print(min_diff)
