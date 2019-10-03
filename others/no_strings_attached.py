#!/usr/bin/python3

for i in range(int(input())) :
    Y = 0
    string = input()
    for l in range(len(string)) :
        for m in range(l, len(string)) :
            if ord(string[l]) < ord(string[m]) :
                Y += 1
    print(Y)

