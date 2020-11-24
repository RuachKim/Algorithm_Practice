n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))


for i in range(1,n):
    for j in range(i+1):

        if j == 0:
            l_up = 0
        else:
            l_up = arr[i-1][j-1]
        
        if j == i:
            up = 0
        else:
            up = arr[i-1][j]

        arr[i][j] = arr[i][j] + max(l_up, up)


print(max(arr[n-1]))