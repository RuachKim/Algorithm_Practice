"""
This is not the case of kruskal algorithm
This is BFS problem...
"""

import sys
from collections import deque
from itertools import combinations

n = int(input())
weight = list(map(int, input().split()))
#print(weight)
w = [0]*(n+1)
for i in range(n):
   w[i+1] = weight[i]



graph = [[] for _ in range(n+1)]
maps = [ [0]*(n+1) for _ in range(n+1) ]

for i in range(n):
    data = list(map(int, input().split()))
    #cnt = data[0]
    for j in data[1:]:
        maps[i+1][j] = 1






def calc_area(candidates):

    area = 0
    for i in candidates:
        area += w[i]

    return area

def find_exclu(candi):
    
    left = []
    ballot = [0]*(n+1)
    for i in range(1,n+1):
        for j in candi:
            if i == j:
                ballot[i] += 1

    for i in range(1,n+1):
        if ballot[i] == 0:
            left.append(i)
                
    
    return left





visit = []
def group_search(candi):

    start = candi[0]

    q = deque()
    q.append(start)
    visit.append(start)
    count = 1
    while q:

        town = q.popleft()

        for x in range(1, n+1):
            if (maps[town][x] == 1) and (x not in visit) and (x in candi):
                q.append(x)
                visit.append(x)
                count += 1

    
    # print(f"visit: {visit} and count: {count}")
    visit.clear()
    if count == len(candi):
        return True
    
    return False


block = [i for i in range(1,n+1)]


INF = int(1e9)
ans = INF

# for row in range(n+1):
#     print(maps[row])

for i in range(1,n//2+1):

    candidates = list(combinations(block,i))


    #print(candidates)
    for candi in candidates:

        left = find_exclu(candi)
        #print(left)
        # print()
        # print(f"A: {candi}, B: {left}")
        
        if group_search(candi) and group_search(left):
            #calculate area diff
            a = calc_area(candi)
            b = calc_area(left)

            # print("PASS")
            # print(f"A: {candi}, B: {left}")
            # print(f"A area: {a}, B area: {b}")

            diff = abs(a-b)

            if ans > diff:
                ans = diff

if ans == INF:
    print(-1)

else:
    print(ans)























