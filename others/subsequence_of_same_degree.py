#!/usr/bin/python3

try :
    T = int(input())
except :
    quit()

for testCase in range(T) :
    N = int(input())
    Arr = dict() # element : [start, end, count]
    i = 0
    max_count = 0
    min_length = N
    for num in input().split() :
        num = int(num)
        if num in Arr :
            start = Arr[num][0]
            end = Arr[num][1]
            count = Arr[num][2]

            Arr[num][2] += count +1
            Arr[num][1] = i
            if count > max_count and i - start +1 < min_length :
                min_length = i - start +1
                max_count = count
        else :
            Arr[num] = [i, i, 1]
        i += 1

    print(Arr)
