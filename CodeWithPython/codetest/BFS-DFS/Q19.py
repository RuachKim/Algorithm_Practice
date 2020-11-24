"""
find the maximum sum using 4 operations
"""

num = int(input())
operand = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

min_value = 1e9
max_value = -1e9


def dfs(i, now):

    global min_value, max_value, add, sub, mul, div

    if i == num:
        min_value = min(min_value, now)
        max_value = max(max_value, now)
    
    else:

        if add > 0:
            add -= 1
            dfs(i+1, now+operand[i])
            add += 1
        
        if sub > 0:
            sub -= 1
            dfs(i+1, now-operand[i])
            sub += 1
        
        if mul > 0:
            mul -= 1
            dfs(i+1, now*operand[i])
            mul += 1

        if div > 0:
            div -= 1
            dfs(i+1, int(now/operand[i]))
            div += 1
    
dfs(1, operand[0])

print(f'min: {min_value}  max: {max_value}')


     
