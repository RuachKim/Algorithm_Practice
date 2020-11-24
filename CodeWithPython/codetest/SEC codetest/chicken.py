from itertools import combinations
import math

n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

chick = []
home = []

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            home.append((i,j))
        elif arr[i][j] == 2:
            chick.append((i,j))

candidate = list(combinations(chick,m))
print(candidate)

def calc_dist(home, candidate):
    dist, sum = 0, 0
    
    for x, y in home:
        m_dist = int(1e9)
        for x1, y1 in candidate:
            dist = abs(x-x1) + abs(y-y1)
            m_dist = min(m_dist, dist)
        sum += m_dist

    return sum


min_v = int(1e9)
for cand in candidate:
    res = calc_dist(home, list(cand))
    print(res)
    min_v = min(res, min_v)

print(min_v)

