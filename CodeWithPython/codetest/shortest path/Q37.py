n = int(input())
bus = int(input())
INF = int(1e9)
data = [[INF]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j:
            data[i][j] = 0

for _ in range(bus):
    a,b,c = map(int, input().split())
    if c < data[a][b]:
        data[a][b] = c

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            data[a][b] = min(data[a][b], data[a][k] + data[k][b])


for i in range(1, n+1):
    for j in range(1, n+1):
        if data[a][b] == INF:
            print(0, end = ' ')
        else:
            print(data[a][b], end = ' ')

    print('\n')




