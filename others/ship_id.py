#!/usr/bin/env python3
id_and_ship = {'B':'BattleShip', 'C':'Cruiser', 'D':'Destroyer', 'F':'Frigate'}
ships = list()

for i in range(int(input())) :
    id = input().upper()
    ships.append(id_and_ship[id])
for ship in ships :
    print(ship)
