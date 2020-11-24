"""
DFS???
"""

from collections import deque

n, L, R = map(int, input().split())

maps= []
for _ in range(n):
    maps.append(list(map(int, input().split())))


dx = [-1,1,0,0]
dy = [0,0,-1,1]   


# : L <= diff <= R, 조건 성립할 때만 탐색 시전

def calc_diff(x,y,nx,ny):

    ans = abs(maps[x][y] - maps[nx][ny])
    if L <= ans <= R:
        #move possible
        return True

    else:
         return False

def rearrange(check):
    cnt = 0
    sums = 0
    for i in range(n):
        for j in range(n):
            if check[i][j] == 1:
                cnt += 1
                sums += maps[i][j]
    
    val = sums // cnt

    for i in range(n):
        for j in range(n):
            if check[i][j] == 1:
                maps[i][j] = val


def draw_maps(arr):
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end =' ')
        print('')


def bfs(x,y,time):

    q = deque()
    q.append((x,y))
     
    check[x][y] = time

    while q:

        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and ny >= 0 and nx < n and ny < n:
                if not check[nx][ny]:
                    if calc_diff(x,y,nx,ny):
                        #pass
                        check[nx][ny] = 1
                        q.append((nx, ny))

    
    cnt = 0
    for i in range(n):
        for j in range(n):
            if check[i][j] == 1:
                cnt += 1
    
    if cnt > 1:
        rearrange(check)
        return True
    
    else:
        return False

cnt = 0
while True:
    time = 0
    check = [[-1]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if check[i][j] == -1:
                bfs(i,j,time)
                time += 1
    
    if time == n*n:
        break

    cnt += 1
#bfs(0,0)
print('')
draw_maps(maps)

print(cnt)




