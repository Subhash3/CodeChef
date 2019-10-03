#!/usr/bin/python3

population = dict()
population = {'bit': 1, 'nibble': 0, 'byte': 0}

for i in range(int(input())) :
    N = int(input())
    population = {'bit': 1, 'nibble': 0, 'byte': 0}
    for j in range(N+1) :
        if j > 16 :
            population['bit'] = 2*population['byte']
            population['byte'] = 0
        if j > 8 :
            population['byte'] = population['nibble']
            population['nibble'] = 0
        if j > 2 :
            population['nibble'] = population['bit']
            population['bit'] = 0

    print(population)


    
