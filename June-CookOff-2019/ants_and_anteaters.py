#!/usr/bin/python3

directions = ['L', 'R', 'U', 'D']

def print_grid(grid) :
    for row in grid :
        print(row)
    return

def str_to_list(string) :
    lst = list()
    for i in string :
        lst.append(i)

    return lst

def get_ants_count(grid, R, C) :
    count = 0
    for i in range(R) :
        for j in range(C) :
            if grid[i][j] in directions :
                count += 1
    return count

def make_move(x, y, grid, meets, R, C, d) :
    if R > x >= 0 and C > y >= 0: # Check if the position is valid
        if grid[x][y] in directions : # if there is an ant in that cell
            meets += 1
        elif grid[x][y] == '#' : # If there is an ant eater
            pass # ant eater eats the ant
        else : # the cell is empty
            grid[x][y] = d
    return

def find_ant_pairs(grid, R, C) :
    meets = 0
    ants_count = 1
    grid_copy = list(grid)
    while ants_count >= 0 :
        grid = grid_copy
        for i in range(R) :
            for j in range(C) :
                print(meets)
                print_grid(grid)
                print()
                print_grid(grid_copy)
                d = grid[i][j]
                # print("grid["+str(i)+"]["+str(j)+"]:", d)
                input()
                if grid[i][j] == 'U' :
                    print("Making an up move")
                    make_move(i-1, j, grid_copy, meets, R, C, d)
                elif grid[i][j] == 'D' :
                    print("Making a down move")
                    make_move(i+1, j, grid_copy, meets, R, C, d)
                elif grid[i][j] == 'R' :
                    print("Making a right move")
                    make_move(i, j+1, grid_copy, meets, R, C, d)
                elif grid[i][j] == 'L' :
                    print("Making a left move")
                    make_move(i, j-1, grid_copy, meets, R, C, d)
                grid_copy[i][j] = '-' # make the cell empty 
        ants_count = get_ants_count(grid, R, C)           
    return meets

try :
    T = int(input())
except :
    quit()

for test_case in range(T) :
    grid = []
    R, C = input().split()
    R = int(R)
    C = int(C)
    for r in range(R) :
        row = str_to_list(input())
        grid.append(row)
    meets = find_ant_pairs(grid, R, C)
    print(meets)
    
