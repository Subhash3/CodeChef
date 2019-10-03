#!/usr/bin/python3

def intersection(s1, s2) :
    common = ""
    for ch1 in s1 :
        for ch2 in s2 :
            if ch1 == ch2 and ch1 not in common:
                common += ch1
                break
    return common

nums = list()
for t in range(int(input())) :
    strings = list()
    for i in range(int(input())) :
        strings.append(input())
        if i == 0 :
            common = strings[i]
        else :
            common = intersection(common, strings[i])
    nums.append(len(common))
for num in nums :
    print(num)
"""
common = strings[0]
for string in strings[1:] :
    common = intersection(common, string)
"""
