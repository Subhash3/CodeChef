#!/usr/bin/python3

global N

def is_valid_block(pair) :
    for c in pair :
        if c >= 0 and c < N :
            # valid = True
            pass
        else :
            return False
    return True

def rook_blocks(x, y) :
    under_attack = list()
    under_attack.append((x, y))

    for i in range(N) :
        under_attack.append((x, i))
        under_attack.append((i, y))
    return set(under_attack)

def knight_blocks(x, y) :
    under_attack = list()
    under_attack.append((x, y))

    possible_moves =  [(x+1, y+2), (x+1, y-2), (x-1, y+2), (x-1, y-2)]
    possible_moves += [(x+2, y+1), (x+2, y-1), (x-2, y+1), (x-2, y-1)]

    for block in possible_moves :
        for block in possible_moves :
            if is_valid_block(block) :
                under_attack.append(block)

    return set(under_attack)

def bishop_blocks(x, y) :
    under_attack = list()
    under_attack.append((x, y))

    for i in range(N) :
        possible_moves = [(x+i, y+i), (x+i, y-i), (x-i, y+i), (x-i, y-i)]
        for block in possible_moves :
            if is_valid_block(block) :
                under_attack.append(block)

    return set(under_attack)

def queen_blocks(x, y) :
    under_attack = list()
    under_attack.append((x, y))

    under_attack += rook_blocks(x, y)
    under_attack += bishop_blocks(x, y)

    return set(under_attack)

N = int(input())
total_blocks = list()
for i in range(N) :
    for j in range(N) :
        total_blocks.append((i, j))
total_blocks = set(total_blocks)

blocks_under_attack = set()

K = int(input())
for i in range(K) :
    x, y = map(int, input().split())
    # blocks_under_attack += knight_blocks(x, y)
    # blocks_under_attack = blocks_under_attack.union(knight_blocks(x, y))
    blocks_under_attack = blocks_under_attack.union(knight_blocks(x-1, y-1))
print(blocks_under_attack)
print("----------------------------------------------")

R = int(input())
for i in range(R) :
    x, y = map(int, input().split())
    # blocks_under_attack += rook_blocks(x, y)
    # blocks_under_attack = blocks_under_attack.union(rook_blocks(x, y))
    blocks_under_attack = blocks_under_attack.union(rook_blocks(x-1, y-1))
print(blocks_under_attack)
print("----------------------------------------------")

B = int(input())
for i in range(B) :
    x, y = map(int, input().split())
    # blocks_under_attack += bishop_blocks(x, y)
    # blocks_under_attack = blocks_under_attack.union(bishop_blocks(x, y))
    blocks_under_attack = blocks_under_attack.union(bishop_blocks(x-1, y-1))

print(blocks_under_attack)
print("----------------------------------------------")

Q = int(input())
for i in range(Q) :
    x, y = map(int, input().split())
    # blocks_under_attack += queen_blocks(x, y)
    # blocks_under_attack = blocks_under_attack.union(queen_blocks(x, y))
    blocks_under_attack = blocks_under_attack.union(queen_blocks(x-1, y-1))

print(blocks_under_attack)
print("----------------------------------------------")

print("\n", len(total_blocks), len(blocks_under_attack))
safe_blocks = total_blocks - blocks_under_attack
print(safe_blocks)
print("----------------------------------------------")
print(len(safe_blocks))
