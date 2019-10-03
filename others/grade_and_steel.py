#!/usr/bin/env python3
for i in range(int(input())) :
    hard, carbon, tensile = map(float, input().split())
    if hard > 50 and carbon < 0.7 and tensile > 5600 :
        print("10")
    elif hard > 50 and carbon < 0.7 and not tensile > 5600 :
        print("9")
    elif not hard > 50 and carbon < 0.7 and tensile > 5600 :
        print("8")
    elif hard > 50 and not carbon < 0.7 and tensile > 5600 :
        print("7")
    elif hard <= 50 and carbon >= 0.7 and tensile <= 5600 :
        print("5")
    else :
        print("6")
