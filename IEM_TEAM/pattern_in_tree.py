#!/usr/bin/python3

n = int(input())
root = input()
adjacency_list = input()
pattern = input()

tree = dict() # node, [connected vertices]
paths = adjacency_list.split(',')
for path in paths :
    # print(path)
    nodes = path.split('->')
    length = len(nodes)
    for i in range(length) :
        cur_node = nodes[i]
        if cur_node not in tree :
            tree[cur_node] = set()
        if i > length-2 :
            break
        next_node = nodes[i+1]
        tree[cur_node].add(next_node)

# print(tree)
pattern_length = len(pattern)
prev_node = None
flag = True
for i in range(pattern_length) :
    node = pattern[i]
    if node not in tree :
        flag = False
        # print(node, "is not there in tree")
        break
    if prev_node != None :
        if node not in tree[prev_node] :
            flag = False
            # print(node, "is not connected to", prev_node)
            break
    prev_node = node
if not flag :
    print(0)
else :
    print(1)