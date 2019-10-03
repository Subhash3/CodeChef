#!/usr/bin/python3

def print_tree(tree) :
    for node in tree :
        print(node.get_root())
        print("\t" + node.children)
    return

class Node :
    children = dict()
    def __init__(self, root) :
        self.root = root
    def get_root(self) :
        return self.root
    def connect(self, child, price) :
        self.children[child] = price
    def min_price(self) :
        keys = list(self.children.keys())
        values = list(self.children.values())
        min_price = min(values)
        city_with_min_price = keys[keys.index(min_price)]
        return city_with_min_price

tree = [] # array of nodes

try :
    C_F = input().split()
    C = int(C_F[0])
    F = int(C_F[1])
    for i in range(F) :
        vals = input().split()
        x = int(vals[0])
        y = int(vals[1])
        p = int(vals[2])
        node_exists = False
        for n in tree :
            # print("Checking if root already exists in the tree")
            if n.get_root() == x :
                node_exists = True
                # print("Root " + str(x) + " already exists")
                node = n
                break
        if node_exists == False :
            print("Creating a new node")
            node = Node(x)
            print("Adding node " + str(x) + " to the tree")
            tree.append(node)

        # print("Connecting cities to the node")
        node.connect(y, p)
        for n in tree :
            print(n.get_root(), n.children)
except Exception as e:
    print(e) 
    quit()