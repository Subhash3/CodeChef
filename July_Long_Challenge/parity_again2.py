#!/usr/bin/python3

def count_bits(num, bit) :
    ones = 0
    # zeroes = 0
    while num > 0 :
        if num % 2 == 1 :
            ones += 1
        num = num // 2
    #     else :
    #         zeroes += 1
    #     num = num // 2
    # if bit == 1 :
    #     count = ones
    # elif bit == 0 :
    #     count == zeroes
    # else :
    #     return None
    # return count
    return ones

try :
    T = int(input())
except :
    quit()


for test_case in range(T) :
    even = 0
    odd = 0
    S = set()
    # print("Initially:", even, odd)
    Q = int(input())
    for query in range(Q) :
        x = int(input())
        # start = time.time()
        elements_to_add = set()
        if x not in S :
            for y in S :
                num = x^y
                # print(num, " is not in set ", elements_to_add)
                elements_to_add.add(num)
                if count_bits(num, 1) % 2 == 0 :
                    even += 1
                else :
                    odd += 1
            elements_to_add.add(x)
            if count_bits(x, 1) % 2 == 0 :
                even += 1
            else :
                odd += 1
            S = S.union(elements_to_add)
        # print(S)
        print(even, odd)
        # print("Time:", time.time()-start)