n = int(input())
dp = []
t = []
p = []
dp = [0]*(n+1)
max_result = 0

for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)


for i in range(n-1,-1,-1):

    time = i + t[i]

    if time <= n:
        dp[i] = max(p[i]+dp[time], max_result)
        max_result = dp[i]

    else:
        dp[i] = max_result

print(dp)
print(max_result)