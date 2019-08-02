import sys
num_v = int(sys.stdin.readline().strip().split()[0])
num_e = int(sys.stdin.readline().strip().split()[0])

Tree = dict()
nodes = set()

for i in range(num_e):
    v0, v1, e01, c01 = sys.stdin.readline().strip().split()
    c01 = int(c01)
    nodes.update(v0)
    nodes.update(v1)
    if v0 in Tree:
        if v1 in Tree[v0]:
            Tree[v0][v1][1].append(e01)
            Tree[v0][v1][0]+= c01
        else:
            Tree[v0][v1] = [c01,[e01]]
    else:
        Tree[v0] = dict()
        Tree[v0][v1] = [c01,[e01]]


#First solve only one circle

def has_circle(Tree):
    global visited 
    visited = set()
    start = list(Tree.keys())
    circle = []

    
    for i in start:
        if not i in visited:
            is_circle(Tree,i,circle,[])
    if circle:
        return circle
    else:
        return False

def is_circle(Tree,node,circle, path):

    if node in path:
        index = path.index(node)
        path.append(node)
        circle.append(path[index:])
    else:
        if node in Tree:
            for item in Tree[node]:
                is_circle(Tree,item,circle,path+[node])
    visited.add(node)

circles = has_circle(Tree)
print(circles)
min_l = float("inf")
res = []
if not circles:
    print("#")
else:
    circles = circles[0]
    print(len(circles)-1)
    for i in range(len(circles)-1):

        if Tree[circles[i]][circles[i+1]][0]<min_l:
            min_l = Tree[circles[i]][circles[i+1]][0]
            res = Tree[circles[i]][circles[i+1]][1]
    print(" ".join(res))


#what if there are multiple circles
 
