from collections import deque
import sys

input = sys.stdin.readline

n,m = map(int, input().split())

maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))


dx = [-1,1,0,0]
dy = [0,0,-1,1]
numbs = 1
check = {}

def find_area(start):
    global numbs
    x,y = start[0],start[1]

    queue = deque()
    queue.append((x,y))
    
    check[start] = 1   
    maps[x][y] = numbs

    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] != 0 and not (nx,ny) in check:
        
                queue.append((nx,ny))
                check[(nx,ny)] = 1
                maps[nx][ny] = numbs  
    
    numbs += 1



for i in range(n):
    for j in range(m):

        if maps[i][j] != 0 and not (i,j) in check:
            start = (i,j)
            find_area(start)


#print(maps)

bridge = []
cnt = 0
for row in maps:
    before = 0
    #print(row)
    for r in row:

        if r != 0 and r != before:
            if before != 0 and cnt > 1:
                if (before, r, cnt) not in bridge:
                    bridge.append((before, r, cnt))
            
            before = r
            cnt = 0
        
        if r == 0:
            cnt += 1

        if r == before:
            cnt = 0


for col in zip(*maps):
    before = 0
    
    for c in col:

        if c != 0 and c != before:
            if before != 0 and cnt > 1:
                if (before, c, cnt) not in bridge:
                    bridge.append((before, c, cnt))
            
            before = c
            cnt = 0
        
        if c == 0:
            cnt += 1

        if c == before:
            cnt = 0


bridge.sort(key = lambda x:x[2])


parent = [i for i in range(numbs)]
rank = [1 for _ in range(numbs)]

def find_parent(i):

    if i != parent[i]:
        return find_parent(parent[i])
    
    return parent[i]

def union(a,b):

    a = find_parent(a)
    b = find_parent(b)

    if a > b:
        parent[a] = b
        rank[b] += rank[a]
    
    else:
        parent[b] = a
        rank[a] += rank[b]

result = 0

for edge in bridge:

    a,b,w = edge

    if find_parent(a) != find_parent(b):
        union(a,b)
        result += w
        

# #print(parent)\


# test = []
# for i in range(1,numbs):
#     test.append(parent[i])



# print(bridge)

if max(rank) != numbs-1:
    result = -1

print(result)

# sol = 0
# def union(v1,v2,w):
#     global sol
#     root1,root2 = find_parent(v1),find_parent(v2)

#     if root1 != root2:
#         sol += w

#         if rank[root1] < rank[root2]:
#             rank[root2] += rank[root1]
#             parent[root1] = root2
#         else:
#             rank[root1] += rank[root2]
#             parent[root2] = root1

# for e in bridge:
#     union(e[0],e[1],e[2])

# if max(rank) != numbs-1:
#     print(-1)
# else:
#     print(sol)

                    
