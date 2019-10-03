#!/usr/bin/python3

try :
    T = int(input())
except :
    quit()

for testCase in range(T) :
    N, Q = map(int, input().split())
    B = list()
    first = True
    possible_Arrs = list()
    for num in input().split() :
        num = int(num)
        B.append(num)
        if first :
            l = 2
            n = 1
            while n < num :
                possible_Arrs.append([n, num-n])
                n += 1 
            length = n-1
            first = False
        else :
            for i in range(length) :
                lst = possible_Arrs[i]
                # print(lst)
                n = lst[-1]
                possible_Arrs[i].append(num -n)
            l += 1
    # print(possible_Arrs)
    for query in range(Q) :
        flag = True
        p, q = map(int, input().split())
        prev_sum = None
        for i in range(length) :
            lst = possible_Arrs[i]
            cur_sum = lst[p-1] + lst[q-1]
            if prev_sum == None :
                prev_sum = cur_sum
            elif prev_sum != cur_sum :
                flag = False
                break
        if flag :
            print(cur_sum)
        else :
            print("UNKNOWN")
