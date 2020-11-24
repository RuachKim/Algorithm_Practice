"""
virus

dfs - bfs
"""
from collections import deque


n = int(input())
m = int(input())


#complete graph
graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


visited = [False]*(n+1)
def dfs(start):

    visited[start] = True

    for edge in graph[start]:

        if visited[edge] == False:
            visited[edge] = True
            dfs(edge)

def bfs(start):
    visited[start] = True
    q = deque()
    q.append(start)

    while q:

        node = q.popleft()

        for edge in graph[node]:
            if not visited[edge]:
                visited[edge] = True
                q.append(edge)




#dfs(1)
bfs(1)
#print(visited)
cnt = 0
for i in range(2, n+1):
    if visited[i] == True:
        cnt += 1


print(cnt)
