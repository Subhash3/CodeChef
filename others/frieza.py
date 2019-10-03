#!/usr/bin/env python3
letters = ['f', 'r', 'i', 'e', 'z', 'a']
R = ''
for i in range(int(input())) :
    user_input = input()
    l = 0
    while l < len(user_input) :
        if user_input[l] in letters :
            count = 0
            while l < len(user_input) :
                if user_input[l] not in letters :
                    break
                else :
                    count += 1
                l += 1
            #R.append(count)
            R += str(count)
        else :
            count = 0
            while l < len(user_input) :
                if user_input[l] in letters :
                    break
                else :
                    count += 1
                l += 1
            #R.append(count)
            R += str(count)
    print(int(R))
    R = ''
