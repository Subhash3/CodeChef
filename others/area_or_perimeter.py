#!/usr/bin/env python3

L = int(input())
B = int(input())

area = L * B
peri = 2*(L + B)
if area < peri :
    print('Peri')
    print(peri)
else :
    print('Area')
    print(area)
