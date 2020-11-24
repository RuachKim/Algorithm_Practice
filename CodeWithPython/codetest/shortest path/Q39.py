import heapq
import sys

input = sys.stdin.readline

INF = int(1e9)
case = int(input())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for tc in range(case):

    n = int(input())
    
    graph = []

    for i in range(n):
        graph.append(list(map(int, input().split())))
    
    distance = [[INF]*n for _ in range(n)]

    x, y = 0, 0

    q = [(graph[x][y], x, y)]
    distance[x][y] = graph[x][y]


    while q:
        dist, x, y = heapq.heappop(q)

        if distance[x][y] < dist:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                cost = graph[nx][ny] + dist
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(q, (distance[nx][ny], nx, ny))
    
    print(distance[n-1][n-1])