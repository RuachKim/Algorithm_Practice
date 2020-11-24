import sys
input = sys.stdin.readline

def find_parent(parent,x):
    if x != parent[x]:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]


def union(parent,a,b):

    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a



n,m = map(int, input().split())
parent = [i for i in range(0,n+1)]

edge = []
for _ in range(m):
    edge.append(list(map(int, input().split())))

edge.sort(key = lambda x:x[2])

res = 0
for dat in edge:
    a, b, w = dat
    if find_parent(parent,a) != find_parent(parent,b):
        union(parent,a,b)
        res += w


print(res)


