#!/usr/bin/python3

MAX_N = 100000

try :
    T = int(input())
except :
    quit()

for testCase in range(T) :
    N = int(input())
    Arr = list()

    num_and_divisible = dict()
    even_numbers = list()

    length = 0
    max_star = None
    max_value = None
    no_of_even = 0
    mod_k_numbers = dict()
    for n in input().split() :
        star = 0
        num = int(n)

        for k in range(2, MAX_N+1) :
            if k > num :
                break
            if k not in mod_k_numbers :
                mod_k_numbers[k] = 0
            else :
                if num%k == 0 :
                    mod_k_numbers[k] += 1

        if max_value == None or max_value < num :
            max_value = num
        Arr.append(num)
        length += 1


        if num == 1 :
            star = length-1
        elif num == max_value :
            pass # If it is the max element, then don't do anthing.
        else :
            for k, count in mod_k_numbers.items() :
                if num == k :
                    star = count
                    if max_star == None or max_star < star :
                        max_star = star
            # print("New Max Star:", new_max_star)
        if max_star == None or max_star < star :
            max_star = star
    print(max_star)
