#!/usr/bin/python3

try :
    T = int(input())
except :
    quit()

for testCase in range(T) :
    vals = input().split()
    L = int(vals[0])
    R = int(vals[1])
    large = None
    # for a in range(L, R+1) :
    #     for b in range(L, R+1) :
    #         num = a | b
    #         if large == None or num > large :
    #             large = num
    # print(num)
    # for num in range(R, L+1, -1) :
    #     a = int(bin(num)[4:], 2)
    #     n = num | a
    #     if large == None or n > large :
    #         large = n
    m = R.bit_length()
    for n in range(L, R+1) :
        l = n.bit_length()
        k = 2**l -1
        if k.bit_length() <= m :
            if large == None or k > large :
                large = k
        # print(k)
        # if L <= k <= R :
    print(large)
