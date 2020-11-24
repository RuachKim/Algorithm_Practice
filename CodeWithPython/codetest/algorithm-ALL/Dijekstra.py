#dijekstra

import heapq

n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a].append((b,w))

INF = int(1e9)
distance = [INF]*(n+1)


def dijekstra(start):

    q = []
    
    distance[start] = 0
    heapq.heappush(q, (0,start))

    while q:

        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            # already visited
                continue
        
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))
    
dijekstra(1)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])


