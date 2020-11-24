from bisect import bisect_left, bisect_right

n, target = map(int, input().split())
data = []
data = list(map(int, input().split()))

def count_by_range(data, l_v, r_v):
    r_index = bisect_right(data, r_v)
    l_index = bisect_left(data, l_v)

    return r_index - l_index


counts = count_by_range(data, target, target)

if counts > 0:
    print(counts)
else:
    print(-1)
