from collections import deque

n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

now_size = 2 #shark size
now_x, now_y = 0, 0
INF = int(1e9)

for i in range(n):
    for j in range(n):
        if data[i][j] == 9:
            now_x = i
            now_y = j
            data[i][j] = 0
            break


def bfs():
    
    q = deque()
    q.append((now_x, now_y))
    distance = [[-1]*n for _ in range(n)]
    distance[now_x][now_y] = 0

    while q:
        x, y = q.popleft()

        for i in range(n):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                if distance[nx][ny] == -1 and data[nx][ny] <= now_size:
                    distance[nx][ny] = distance[x][y] + 1
                    q.append((nx, ny))

    return distance

def find_fish(distance):

    dist_min = INF
    x, y = 0, 0
    for i in range(n):
        for j in range(n):
            if distance[i][j] != -1 and 0 < data[i][j] and data[i][j] < now_size:
                if distance[i][j] < dist_min:
                    dist_min = distance[i][j]
                    x, y = i, j

    if dist_min == INF:
        return None
    else:
        return dist_min, x, y


eaten = 0
time = 0

while True:

    value = find_fish(bfs())

    if value == None:
        print(time)
        break
    
    else:
        time += value[0]
        eaten += 1

        now_x = value[1]
        now_y = value[2]

        data[now_x][now_y] = 0

        if eaten >= now_size:
            eaten = 0
            now_size += 1
    




