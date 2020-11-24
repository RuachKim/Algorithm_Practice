import sys
from collections import deque

n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
def dfs(x, y, direction):
    global cnt

    if x == n-1 and y == n-1:
        cnt += 1
    if direction == 1 or direction == 2:
        #가로 #대각선
        if y+1 < n:
            if maps[x][y+1] == 0:
                dfs(x,y+1,1)
        
    if direction == 1 or direction == 2 or direction == 3:
        #가로 #대각선 #세로
        if x+1 < n and y+1 < n:
            if maps[x+1][y] == maps[x][y+1] == maps[x+1][y+1] == 0:
                dfs(x+1, y+1, 2)
    
    if direction == 2 or direction == 3:
        if x+1 < n:
            if maps[x+1][y] == 0:
                dfs(x+1, y, 3)


def bfs(x,y,direction):
    global cnt

    q = deque()
    q.append((x,y,direction))

    while q:
        x, y, direction = q.popleft()
        #print(f"({x},{y},{direction}")

        if x == n-1 and y == n-1:
            cnt += 1
        if direction == 1 or direction == 2:
            #가로 #대각선
            if y+1 < n:
                if maps[x][y+1] == 0:
                    q.append((x,y+1,1))
            
        if direction == 1 or direction == 2 or direction == 3:
            #가로 #대각선 #세로
            if x+1 < n and y+1 < n:
                if maps[x+1][y] == maps[x][y+1] == maps[x+1][y+1] == 0:
                    q.append((x+1,y+1,2))
        
        if direction == 2 or direction == 3:
            if x+1 < n:
                if maps[x+1][y] == 0:
                    q.append((x+1,y,3))



dfs(0,1,1)
#bfs(0,1,1)

print(cnt)