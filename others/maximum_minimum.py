#!/usr/bin/python3

def get_min_cost(array) :
    minimum = min(array)
    min_cost = minimum*(len(array)-1)
    return min_cost

try :
    test_cases = int(input())
except :
    quit()

for case in range(test_cases) :
    try :
        N = int(input())
        array = input().split()
        array = [int(i) for i in array]
        min_cost = get_min_cost(array)
        print(min_cost)
    except :
        quit()

# Algorithm
"""
Goal is to find the minimum cost.
cost = smaller value of the operation
operation = pick a pair of adjacent numbers, and remove the larger one, the smaller one is the cost
Do this until the array is left with a single element
The sum of costs should be minimum.

To do this we have to select the pair, so that the smaller of those two is the least of the array.

Eg: A = [1, 5, 4, 2]
    cost = 0
    pair = [1, 5] => cost = 1 and A = [1 ,4, 2]
    pair = [1, 4] => cost = 2 and A = [1, 2]
    pair = [1, 2] => cost = 3 and A = [1]

If we pick an ther pair..
    cost = 0
    pair = [4, 2] => cost = 2 and A = [1, 5, 2]
    pair = [5, 2] => cost = 4 and A = [1, 2]
    pair = [1, 2] => cost = 5 and A =[1]

minimum of the costs is 3., i.e in first case.

Therefore, calculate the minimum and add it to itself n-1 times where n is the size of array
"""