#!//usr/bin/python3

for i in range(int(input())) :
    N = int(input())
    P = 1
    if N % 2 == 0 :
        Q = 10 ** (N/2)
    else :
        Q = 10 ** ((N - 1)/2)
    print(P, int(Q))
        
