n, c = map(int, input().split())
house = []
for _ in range(n):
    house.append(int(input()))

house.sort()

start = house[1] - house[0] #min
end = house[-1] - house[0] #max
result = 0 # the maximum gap between adjcent routers

while(start <= end):

    mid = (start+end)//2
    cnt = 1 # number of routers
    crp = house[0] #current router locates

    for i in range(n):
        if house[i] >= crp + mid:
            cnt += 1
            crp = house[i]
    
    if cnt >= c:

        start = mid + 1 # increase the gap
        result = mid
    else:
        end = mid - 1 # decrease the gap


print(result)