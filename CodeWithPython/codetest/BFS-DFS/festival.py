import sys
from collections import deque
input = sys.stdin.readline

t = int(input())


dx = [-1,1,0,0]
dy = [0,0,-1,1]

visited = []
store = []
beer = 20

def distance():
    dist = 0
    for i in range(n+2):
        for j in range(n+2):
            if i == j:
                continue

            dist = abs(point[i][0]-point[j][0]) + abs(point[i][1]-point[j][1]) 
            if dist <= 1000:
                graph[i][j] = 1


def dfs(start):

    visited[start] = True

    for j in range(n+2):
        if graph[start][j] == 1 and not visited[j]:
            dfs(j)

    

for tc in range(t):

    n = int(input()) #store

    point = [list(map(int, input().split())) for _ in range(n+2)]

    visited = [False]*(n+2) 

    graph = [[0]*(n+2) for _ in range(n+2)]

    distance()

    dfs(0)

    if visited[n+1] == True:
        print('happy')
    else:
        print('sad')


