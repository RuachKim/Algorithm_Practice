"""
population moving away
"""

from collections import deque


n, l, r = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]



def moving(x, y,index):
    joint = []
    joint.append((x,y))

    q = deque()
    q.append((x,y))
    union[x][y] = index
    summary = data[x][y]
    count = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < n and union[nx][ny] == -1:
                if l <= abs(data[x][y] - data[nx][ny]) <= r:
                    union[nx][ny] = index
                    joint.append((nx,ny))
                    summary += data[nx][ny]
                    q.append((nx,ny))
                    count += 1

    for i, j in joint:
        data[i][j] = summary//count
    


total_cnt = 0

while True:

    index = 0

    union = [[-1]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                moving(i,j,index)
                index += 1
    
    if index == n*n:
        break

    total_cnt += 1
    

print(total_cnt)
