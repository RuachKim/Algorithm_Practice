"""
DFS example
recursive
"""
#node갯수 : 5 
visited = []
def dfs(start):

    #visited
    visited.append(start)

    for i in graph[start]:
        if i not in visited:
            dfs(i)


"""
BFS example
Queue - check all available nodes from a node 
"""
#DEQUEUE
from collection import deque
visited = []
def bfs(start):

    q = deque()
    q.append(start)
    visited.append(start)
    while q:

        dat = q.pop()

        for i in graph[dat]:
            if i not in visited:
                visited.append(i)
                q.append(i)


 


