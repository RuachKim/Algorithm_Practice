n,m,h = map(int, input().split())

bridge = [False*n for _ in range(m)]

for _ in range(h):
    a, b = map(int, input().split())
    bridge[a-1][b-1] = True



def check():

    for start in range(n):
        k = start
        for i in range(m):
            if bridge[i][k]:
                k += 1
            elif bridge[i][k-1] and k > 0:
                k -= 1
        if start != k:
            return False
    return True

def dfs(cnt, x, y):

    global ans
    if check():
        ans = min(ans, cnt)
        return

    elif cnt == 3 or ans <= cnt:
        return
    

    for i in range(x, h):
        k = y if i==x else 0
        for j in range(k, n-1):
            if not bridge[i][j] and not bridge[i][j+1]:
                bridge[i][j] = True
                dfs(cnt+1, i, j+2)
                bridge[i][j] = False 