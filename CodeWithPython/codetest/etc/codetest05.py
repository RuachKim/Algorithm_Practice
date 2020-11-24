# data structure : queue - deque
    # from collections import deque

    # queue = deque()
    # queue.append(3)
    # queue.append(5)
    # queue.append(2)
    # queue.append(4)

    # queue.popleft()
    # print(queue)
    # queue.reverse()
    # print(queue)

"""
2-dim matrix
"""

# a = [[1]*5 for _ in range(5)]
# print(a)

# print(a[3][1])

"""
DFS/BFS
01 - DFS
"""

# def dfs(graph, cur, visited):
#     visited[cur] = True #check visitor
#     print(cur, end = "-")

#     for i in graph[cur]:
#         if not visited[i]:
#             dfs(graph, i, visited)



# visited = [False]*7
# graph = [[],[2,3],[1,5],[1,4,6],[3],[2,6],[3,5]]
# dfs(graph, 1, visited)


"""
DFS/BFS
02 - BFS
"""
# from collections import deque

# def bfs(graph, cur, visited):
#     queue = deque()
#     visited[cur] = True
#     queue.append(cur)

#     while queue:
        
#         v = queue.popleft()
#         print(v, end = ' ')
#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True


# visited = [False]*7
# graph = [[],[2,3],[1,5],[1,4,6],[3],[2,6],[3,5]]
# bfs(graph, 1, visited)

"""
count the number of iced beverage - DFS  / BFS
"""

#  dx = [0, 0, -1, 1]
#  dy = [-1, 1, 0, 0]

# def dfs(array, cur_x, cur_y, visit):
    
#     if not array[cur_x][cur_y]: 
#         visit[cur_x][cur_y] = 1
        
#     for i in ragne(4):
#         nx = cur_x + dx[i]
#         ny = cur_y + dy[i]

        
#         if not visit[nx][ny] and not array[cur_x][cur_y]:
#             cur_x = nx
#             cur_y = ny
            
#             dfs(array, cur_x, cur_y, visit)

#     return True        





# n, m = map(int, input().split())

# visit = [[0]*m for _ in range(n)]
# #print(visit)
# array = []
# for i in range(n):
#     array.append(list(map(int,input().split())))


# cnt = 0
# for x in range(n):
#     for y in range(m): 
#         res = dfs(array, x, y, visit)
#         if res = True:
#             cnt += 1

# print(cnt)




"""
How the book solves
"""
# n, m = map(int, input().split())

# #visit = [[0]*m for _ in range(n)]
# #print(visit)
# array = []
# for i in range(n):
#     array.append(list(map(int,input().split())))


# def dfs(cur_x, cur_y):

#     if cur_x <= -1 or cur_y <= -1 or cur_x >= n or cur_y >= m:
#         return False
#     if array[cur_x][cur_y] == 0:
#         array[cur_x][cur_y] = 1

#         dfs(cur_x+1,cur_y)
#         dfs(cur_x-1,cur_y)
#         dfs(cur_x, cur_y-1)
#         dfs(cur_x, cur_y+1)

#         return True
    
#     return False


# cnt = 0
# for x in range(n):
#     for y in range(m): 
#         res = dfs(x, y)
#         if res == True:
#             cnt += 1

# print(cnt)


"""
maze runner - BFS
Find the shortest path(# of blocks) to arrive goal
"""

# from collections import deque

# n, m = map(int, input().split())

# graph = []
# for i in range(n):
#     graph.append(list(map(int, input())))

# #print(graph)

# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]

# def bfs(start_x, start_y):

#     queue = deque()
#     queue.append((start_x, start_y))

#     while queue:

#         x, y = queue.popleft()

#         for i in range(4):

#             nx = x + dx[i]
#             ny = y + dy[i]

#             if nx < 0 or nx >= n or ny < 0 or ny >= m:
#                 continue

#             if graph[nx][ny] == 0:
#                 continue

#             if graph[nx][ny] == 1:
#                 graph[nx][ny] = graph[x][y] + 1
#                 queue.append((nx,ny))

#     return graph[n-1][m-1]


# print(bfs(0,0))

"""
Test - BFS basic
"""

# from collections import deque

# n, m = map(int, input().split())

# #graph = [list(map(int,input())) for _ in range(n)]
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input())))

# dx = [ 0,0,-1,1 ]
# dy = [ -1,1, 0, 0]


# def bfs(x, y):

#     queue = deque()
#     queue.append((x,y))

#     while queue:

#         x, y = queue.popleft()

#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if nx < 0 or ny < 0 or nx >= n or ny >= m:
#                 continue

#             if graph[nx][ny] == 0:
#                 continue

#             if graph[nx][ny] == 1:

#                 graph[nx][ny] = graph[x][y] + 1
#                 queue.append((nx,ny))
    
#     return graph[n-1][m-1]


# print(bfs(0,0))











    



