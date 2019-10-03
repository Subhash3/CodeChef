#!/usr/bin/env python3
T = int(input())
if 1 <= T <= 1000 :
    for i in range(T) :
        salary = int(input())
        if 1 <= salary <= 100000 :
            if salary < 1500 :
                hra = salary * 0.1
                da = salary * 0.9
            else :
                hra = 500
                da = salary * 0.98
            print(salary + hra + da)
