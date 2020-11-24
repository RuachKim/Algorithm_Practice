"""
competitional contamination
"""
from collections import deque


n, k = map(int, input().split())

data = []
for i in range(n):
    data.append(list(map(int, input().split())))

t_s, t_x, t_y = map(int, input().split())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

v_map = []

for i in range(n):
    for j in range(n):
        if data[i][j] != 0:
            v_map.append((data[i][j], 0, i, j))


v_map.sort()


q = deque(v_map)

while q:

    virus, t, x, y = q.popleft()

    if t == t_s:
        break

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if data[nx][ny] == 0:
                data[nx][ny] = virus
                q.append((data[nx][ny], t+1, nx, ny))


#print(data[t_x-1][t_y-1])
print(data)







