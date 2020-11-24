"""
searching for shortest path
"""
from collections import deque

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

dist = [-1]*(n+1)
dist[x] = 0

queue = deque([x])

while queue:
    now = queue.popleft()

    for next_node in graph[now]:
        if dist[next_node] == -1: # not visited yet
            dist[next_node] = dist[now] + 1
            queue.append(next_node)


chk = False
for i in range(1,n+1):
    if dist[i] == k:
        print(i)        
        chk = True

if chk is False:
    print(-1)


       