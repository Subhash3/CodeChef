#!/usr/bin/python3

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
    for n in input().split() :
        star = 0
        num = int(n)
        if num%2 == 0 :
            even_numbers.append(num)
            no_of_even += 1

        if max_value == None or max_value < num :
            max_value = num
        Arr.append(num)
        length += 1

        if num == 1 :
            star = length-1
        elif num == 2 :
            star = no_of_even -1
        elif num == max_value :
            pass # If it is the max element, then don't do anthing.
        else :
            if num%2 == 0 : #even :
                star = -1
                array = even_numbers
                for k in even_numbers :
                    if k%num == 0 :
                        star += 1
            else :
                star = 0
                for i in range(length-2, -1, -1) :
                    if Arr[i]%num == 0:
                        star += 1
        if max_star == None or max_star < star :
            max_star = star
    print(max_star)
