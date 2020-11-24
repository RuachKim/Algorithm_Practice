"""
memoization of fibonacci
"""
d = [0]* 100
def fibonacci(x):
    if x <= 2:
        return 1

    if d[x] != 0:
        return d[x]

    d[x] = fibonacci(x-1) + fibonacci(x-2)

    return d[x]


ans = fibonacci(4)
print(ans)

    
