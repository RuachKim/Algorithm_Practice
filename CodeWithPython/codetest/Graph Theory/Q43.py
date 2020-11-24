def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    
    return parent[x]

def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    

n, m = map(int, input().split())

parent = [0] * (n+1)

for i in range(n+1):
    parent[i] = i


graph = []
for _ in range(m):
    x, y, cost = map(int, input().split())
    graph.append((cost, x, y))

total = 0
price = 0

graph.sort()

for road in graph:
    cost, x, y = road
    total += cost
    if find_parent(parent, x) != find_parent(parent, y):
        union(parent, x, y)
        price += cost

print(total - price)