"""
find each area(section)

0 1 1 0 0 0 
0 1 1 0 1 1 
0 0 0 0 1 1 
0 0 0 0 1 1 
1 1 0 0 1 0   
1 1 1 0 0 0 
"""

from collections import deque

n = int(input())

maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

visit = [[0]*n for _ in range(n)]
area = 1
ans = [0]*(n*n)

def bfs(start):
    global area

    x, y = start
    q = deque()
    visit[x][y] = area 
    q.append(start)
    cnt = 1
    #print(q)

    while q:

        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < n and 0<= ny < n and visit[nx][ny] == 0 and maps[nx][ny] == 1:
                q.append((nx,ny))
                visit[nx][ny] = area
                cnt += 1
        
    print(f"area:{area}, cnt:{cnt}")
    ans[area] = cnt
    area += 1



for i in range(n):
    for j in range(n):

        if maps[i][j] == 1 and visit[i][j] == 0:
            start = (i,j)
            bfs(start)


for i in range(n):
    print(visit[i])



if area == 0:
    print(0)

else:
    print(area-1)

    result = [0]*(area)
    for i in range(area):
        result[i] = ans[i]

    result.sort()

    for i in range(1,area):
        print(result[i], end= ' ')

            


