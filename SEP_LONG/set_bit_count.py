#!/usr/bin/python3

def number_of_set_bits(x) :
    count = 0
    while x > 0 :
        if x % 2 == 1 :
            count += 1
        x = x // 2
    return count

# try :
#     T = int(input())
# except :
#     quit()

N = int(input("Enter N: "))

count_and_numbers = dict()
for i in range(1, N) :
    count = number_of_set_bits(i)
    # print(i, count)
    if count in count_and_numbers :
        count_and_numbers[count].append(i)
    else :
        count_and_numbers[count] = [i]

# print(count_and_numbers)
for k, v in count_and_numbers.items() :
    print(k, v)
