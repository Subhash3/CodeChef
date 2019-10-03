#!/usr/bin/python3

def power(x, y) : 
    res = 1
  
    while (y > 0) : 
        if ((y & 1) == 1) : 
            res = res * x
  
        y = y >> 1
        x = x * x
          
    return res 

x, y = map(int, input("Enter base and exponent: ").split())
print(power(x, y))