import random

n,m = map(int, input().split())

home = []
chick = []
closed = []
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))


def calc_dist():
    dist = 0
    m_dist = int(1e9)
    d_sum = 0
    for h in home:
        x, y = h
        for c in chick:
            x1, y1 = c
            dist = abs(x-x1) + abs(y-y1)
            m_dist = min(dist, m_dist)
        
        d_sum += m_dist

    return  d_sum

# def close_chain(arr, num):

     
#         closed = random.sample(chick, num)
#         for chain in closed:
#             x, y = chain
#             arr[x][y] = 0

# def open_chain(arr):

#     for place in closed:
#         x, y = place
#         arr[x][y] = 2

def check_map(arr):

    chick.clear()
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                chick.append((i,j))

def dfs(arr, cnt):

    global ans, total_dist, total
    
    if cnt <= m:
        print("here")
        print(f"cnt:{cnt}, m:{m}")
        
        ans = min(ans, total_dist)
        return
    
    
    #total_dist = calc_dist()
    #print(f"{cnt}:{total_dist}")
    print(f"total_dist, cnt = {total_dist}, {cnt}")
    check_map(arr)
    total_dist = calc_dist()
#    close_chain(arr,cnt)
    closed = random.sample(chick,1)
    x, y = closed[0]
    arr[x][y] = 0
    
    dfs(arr, cnt-1)
    arr[x][y] = 2
#    open_chain(arr)



#cnt is the nmber of current store
ans = int(1e9)
total_dist = 0
total = 0
store = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            home.append((i,j))
            total += 1
        elif arr[i][j] == 2:
            store += 1    
check_map(arr)
total_dist = calc_dist()
dfs(arr, store)

print(ans)


        
    #DFS - methodlogy



# 치킨집 선정
def find(idx, x, y):
    global ans
    if(idx == m):
        r = []
        for i in range(n):
            for j in range(n):
                if(arr[i][j] == 3):
                    r.append((i,j))
        res = far(r, house)
        if(ans > sum(res)):
            ans = sum(res)
        return
    else:
        for i in range(x, n):
            if(i == x):
                k = y
            else:
                k = 0
            for j in range(k, n):
                if(arr[i][j] == 2):
                    arr[i][j] = 3
                    find(idx+1, i, j+1)
                    arr[i][j] = 2


# 도시의 치킨거리 구해주기
def far(c, h):
    res = []
    for i in h:
        minV = 999999
        for j in c:
            fars = abs(i[0]-j[0]) + abs(i[1]-j[1]) 
            minV = min(minV, fars)
        res.append(minV)
    return res

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = 99999
# 0 = 빈칸 // 1 = 집 // 2 = 치킨집
# 집 찾기, 치킨집 개수 찾기
chicken = 0
house = []
for i in range(n):
    for j in range(n):
        if(arr[i][j] == 1):
            house.append((i,j))
        elif(arr[i][j] == 2):
            chicken += 1

find(0,0,0)
print(ans)
