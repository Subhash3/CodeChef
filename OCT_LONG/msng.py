#!/usr/bin/python3

def to_decimal(string, base, known_value) :
    l = len(string)

    num = 0
    i = 0
    for i in range(l) :
        try :
            digit = int(string[i])
        except :
            digit = ord(string[i]) -ord('A') +10

        if digit >= base :
            # print("HIH", digit, base)
            return None
        num += digit*(base**(l-i-1))

    return num

try :
    T = int(input())
except :
    quit()

for testCase in range(T) :
    N = int(input())

    known_value = None
    common_values = list()
    for i in range(N) :
        val = input().split()
        B = int(val[0])
        Y = val[1]
        possible_values = dict()
        if B != -1 :
            if B == 10 :
                known_value = int(Y)
            else :
                known_value = to_decimal(Y, B, known_value)
            if i == 0 :
                common_values.append(known_value)
        else :
            for base in range(2, 37) :
                X = to_decimal(Y, base, known_value)
                # print(Y, base, X)
                if Y not in possible_values :
                    possible_values[Y] = []
                if X != None :
                    possible_values[Y].append((base, X))
            if i == 0 :
                common_values = possible_values[Y]
            else:
                common_values = list(set(common_values) & set(possible_values))
            print("Common values: ", common_values)       
        # print(possible_values)
