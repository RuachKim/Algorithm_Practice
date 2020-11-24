"""
brute force problem
"""


def growth(tree_map, tree_loc):

    dead = []
    
    for x, y, age in tree_loc:
        
            if tree_map[x][y][0] >= age: 
                tree_map[x][y][0] -= age
                tree_map[x][y][1] += 1 # number of tree
        
            else:
                tree_map[x][y][1] -= 1 #die
                dead.append((x,y,age))

    return dead
            

def breeding():

    return

def nourishing():

    return

def numoftree():

    return



n, m, k = map(int, input().split())

arr = [] # resource be added in winter
for _ in range(n):
    arr.append(list(map(int, input().split())))

tree_map = [[(5,0)]*n for _ in range(n)]

tree_loc = [] # location(x,y), age
for _ in range(m):
    tree_loc.append(list(map(int, input().split())))
    
    



dx = [1,0,-1,-1,-1,0,1,1]
dy = [-1,-1,-1,0,1,1,1,0]




