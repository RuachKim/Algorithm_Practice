"""
Dynamic programming - **Bottom Up / Top Down

Typical Quiz - Fibonacci
We can solve this problem with 2 ways

The problem below is regarding to making '1' using one of 4 functions
"""

# # first input
# x = int(input())

# d = [0]*30001 # count of operation

# for i in range(2, x+1):
#     """
#     this function is always available, and the reason why +1 is because of count of operation
#     """
#     d[i] = d[i-1] + 1 

#     if i % 2 == 0:
#         d[i] = min(d[i], d[i//2]+1) # comparison with /2
    
#     if i % 3 == 0:
#         d[i] = min(d[i], d[i//3]+1) # with /3
#     if i % 5 == 0:
#         d[i] = min(d[i], d[i//5]+1) # with /5


# print(d[x])

"""
Dynamic programming - **Bottom Up / Top Down

Typical Quiz - Fibonacci
We can solve this problem with 2 ways

The problem below is regarding to \"warrior\", find the maximum golden we get
"""
# n = int(input())
# array = list(map(int, input().split())) #array[0...n-1] -> n

# d = [0]*100

# d[0] = array[0]
# d[1] = max(array[0], array[1])

# for i in range(2, n): #watch out the boundary 
#     d[i] = max(d[i-1], d[i-2]+array[i])


# print(d[n-1])

"""
Dynamic programming - **Bottom Up / Top Down

The problem below is regarding to \"Tile\", find the all the number of tiles to fill the space
"""

# n = int(input())

# d = [0]*1001

# d[1] = 1
# d[2] = 2

# for i in range(3,n+1):
#     d[i] = (d[i-1] + d[i-2]*2) % 796796

# print(d[n])

"""
Dynamic programming - **Bottom Up / Top Down

The problem below is regarding to \"Money\", find the minimum number of coins to make goal.
"""
n, m = map(int, input().split())
array = []
for i in range(n): 
    array.append(int(input()))

#print(array)

d = [10001]*(m+1)

d[0] = 0
#print(d)

for i in range(n):
    for j in range(array[i], m+1):
        if d[j-array[i]] != 10001:
            d[j] = min(d[j], d[j-array[i]]+1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])