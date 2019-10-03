#!/usr/bin/python3

for test_case in range(int(input())) :
    N_K = input().split()
    N = int(N_K[0])
    K = int(N_K[1])
    kombat_powers = input().split()
    for i in range(len(kombat_powers)) :
        kombat_powers[i] = int(kombat_powers[i])
    chef_powers = input().split()
    for i in range(len(kombat_powers)) :
        chef_powers[i] = int(chef_powers[i])

    chef_powers.sort()
    kombat_powers.sort()

    count = 0
    for chef in chef_powers :
        for kombat in kombat_powers :
            if chef > kombat :
                kombat_powers.pop(kombat_powers.index(kombat))
                count += 1
            else :
                break
        if count >= K :
            print("YES")
            break
    if count < K :
        print("NO")

