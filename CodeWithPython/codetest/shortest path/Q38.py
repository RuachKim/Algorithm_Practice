"""
Floyd Warshall Algorithm
"""

n, m = map(int, input().split())
INF = int(1e9)

arr = [[INF]*(n+1) for _ in range(n+1)]


for i in range(n+1):
    for j in range(n+1):
        if i == j:
            arr[i][j] = 0


for _ in range(m):
    a, b = map(int, input().split())
    arr[a][b] = 1


for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])


result = 0
for i in range(1,n+1):
    cnt = 0
    for j in range(1, n+1):
        if arr[i][j] != INF or arr[j][i] != INF:
            cnt += 1
    if cnt == n:
        result += 1


print(result)
