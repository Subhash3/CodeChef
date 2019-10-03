#!/usr/bin/env python3

result = list()

for i in range(int(input())) :
    numbers = input().split()
    if int(numbers[0]) > int(numbers[1]) :
        result.append(">")
    elif int(numbers[0]) < int(numbers[1]) :
        result.append("<")
    else :
        result.append("=")
for x in result :
    print(x)
