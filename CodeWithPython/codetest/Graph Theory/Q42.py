def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    
    return parent[x]

def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a


g = int(input())
p = int(input())
parent = [0] * (g+1)

for i in range(g+1):
    parent[i] = i



d = []
for _ in range(p):
    d.append(int(input()))

result = 0

for i in range(p):
    dat = find_parent(parent, d[i])
    if dat == 0:
        break
    
    union(parent, dat, dat-1)
    result += 1

print(result)

