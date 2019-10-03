#!/usr/bin/python3

def compare_strings(first, second) :
    for i in range(len(first)) :
        matched = "No"
        if first[i] == '?' or second[i] == '?' or first[i] == second[i] :
            matched = "Yes"
        else :
            matched = "No"
            break
    return matched

try :
    test_cases = int(input())
except :
    quit()
for case in range(test_cases) :
    first_str = input()
    second_str = input()

    matched = compare_strings(first_str, second_str)
    print(matched)