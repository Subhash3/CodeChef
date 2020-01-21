#!/usr/bin/python3

MAX_X = 1000000000000

def to_decimal(string, base) :
    try :
        return int(string, base)
    except :
        return None

def decimal_to_base(num, base) :
    base_string = ""
    current_num = num
    
    while current_num :
        mod = current_num % base
        current_num = current_num // base
        base_string = chr(48 + mod + 7*(mod > 10)) + base_string
    return base_string

try :
    T = int(input())
except :
    quit()

for testCase in range(T) :
    N = int(input())
    
    known_decimal = None
    string_and_base_values = dict()
    strings = list()
    given_input = list()

    flag = True
    common = set()
    for i in range(N) :
        values = input().split()
        given_input.append(values)
        B = int(values[0])
        Y = values[1]
        strings.append(Y)

        if B != -1 :
            if known_decimal != None :
                # new_known_decimal = to_decimal(Y, B)
                new_known_decimal = int(Y, B)
                if new_known_decimal != known_decimal :
                    flag = False
            known_decimal = to_decimal(Y, B)
    # Now we have a known decimal value
    if known_decimal != None :
        if not flag :
            print(-1)
        else :
            known_value_in_all_bases = list()
            for base in range(2, 37) :
                base_string = decimal_to_base(known_decimal, base)
                known_value_in_all_bases.append(base_string)
            # print("Known value", known_decimal, "in all bases", known_value_in_all_bases)

            flag = True
            for s in strings :
                if s not in known_value_in_all_bases :
                    flag = False
                    break
            if not flag :
                print(-1)
            else :
                if known_decimal > MAX_X :
                    print(-1)
                else :
                    print(known_decimal)
    else :
        first = True
        for values in given_input :
            B = int(values[0])
            Y = values[1]

            base_values = set()

            for base in range(2, 37) :
                # base_value = to_decimal(Y, base)
                # if base_value != None :
                #     base_values.add(base_value)
                try :
                    base_value = int(Y, base)
                    base_values.add(base_value)
                except :
                    pass
            string_and_base_values[Y] = base_values
            if first :
                common = base_values
                first = False
            else :
                common = common.intersection(base_values)
            # print(string_and_base_values)
            # print("Common:", common)
            # print()

        if common == set() :
            print(-1)
        else :
            smallest = None
            for num in common :
                if smallest == None or num < smallest :
                    smallest = num
            if smallest > MAX_X :
                print(-1)
            else :
                print(smallest)
