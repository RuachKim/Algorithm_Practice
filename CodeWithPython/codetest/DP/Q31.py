case = int(input())
answer = []
for tc in range(case):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    dp = []
    index = 0

    #make dp map (copy arr to dp)
    for i in range(n):
        dp.append(arr[index:index+m])
        index += m
    
    #remap the dp
    for j in range(1,m):
        for i in range(n):

            if i == 0:
                left_up = 0
            else:
                left_up = dp[i-1][j-1]

            if i == n-1: 
                left_down = 0
            else:
                left_down = dp[i+1][j-1]
            
            left = dp[i][j-1]
            dp[i][j] = dp[i][j] + max(left_up, left, left_down)
    
    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1])
    
    answer.append(result)

for i in range(case):
    print(answer[i])
