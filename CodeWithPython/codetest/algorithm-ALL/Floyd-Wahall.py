"""
Floyd-Washall algorithm
idea : create matrix node by node, init with infinity numbers
but for given edges. and then 
"""

INF = int(1e9)
n,m = map(int, input().split())
maps = [[INF]*(n+1) for _ in range(n+1)]

for i in range(n+1):
    for j in range(n+1):
        if i == j:
            maps[i][j] = 0


for _ in range(m):
    a,b,w = map(int, input().split())
    maps[a][b] = w


for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):

            maps[i][j] = min(maps[i][j], maps[i][k] + maps[k][j])


for i in range(1,n+1):
    for j in range(1,n+1):

        if maps[i][j] == INF:
            print('INF')
        else:
            print(maps[i][j], end = ' ')
    
    print()
    









