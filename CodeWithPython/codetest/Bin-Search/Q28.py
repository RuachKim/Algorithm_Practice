from bisect import bisect_left, bisect_right

n = int(input())
data = list(map(int, input().split()))

def find_fixp(data, n):
    
    for i in data:
        a = bisect_left(data, i)
        if a == i:
            return a
            break

    return -1

print(find_fixp(data,n))
