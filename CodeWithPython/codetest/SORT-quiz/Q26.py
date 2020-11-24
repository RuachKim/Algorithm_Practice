import heapq

n = int(input())
heap = []
for _ in range(n):
    data = int(input())
    heapq.heappush(heap,data)

res = 0

while len(heap) != 1:
    
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    c = a+b
    res += c
    #print(f"sum = {c}")
    heapq.heappush(heap,c)

print(res)