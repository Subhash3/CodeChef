#!/usr/bin/python3

def sum_div(n, L, R) : # Sum of numbers divisible by n
    if R <  L :
        R, L = L, R
    factors = list()
    for num in range(L, R+1) :
        if num % n == 0 :
            factors.append(num)
    return sum(factors)

def gcd(x, y):
   while y :
       x, y = y, x % y

   return x

def lcm(x, y):
   lcm = (x*y)//gcd(x,y)
   return lcm

try :
    test_cases = int(input())
except :
    quit()

for case in range(test_cases) :
    A, B, L, R = input().split()
    SA = sum_div(int(A), int(L), int(R))
    SB = sum_div(int(B), int(L), int(R))
    PS = SA + SB
    LCM = lcm(int(A), int(B))
    SL = sum_div(LCM, int(L), int(R))
    print(SA, SB, PS, LCM, SL, abs(PS-SL))
    if (abs(PS-SL) % 2 == 0) and (abs(PS-SL) %3 == 0) :
        print("TRUE LOVE")
    elif (PS % 2 == 0) or (PS % 3 == 0) :
        print("LOVE")
    else :
        print("FAKE LOVE")

# def lcm(x, y):
#    if x > y:
#        greater = x
#    else:
#        greater = y

#    while True:
#        if (greater % x == 0) and (greater % y == 0) :
#            lcm = greater
#            break
#        greater += 1

#    return lcm