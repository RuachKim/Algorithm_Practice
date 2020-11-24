n = int(input())
arr = list(map(int, input().split()))

dp = [1]*n #array[i]를 끝으로 하는 연속된 수의 누적 개수

for i in range(1,n):
    for j in range(i):
        if arr[i] < arr[j]:
            dp[i] = max(dp[i], dp[j]+1)


ans = max(dp)
print(n-ans)
