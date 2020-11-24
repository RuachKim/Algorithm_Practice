print('hello World')

# """
# Floyds' Tortoise and Heare
# -Find Duplicates
# """

# def find_dup(data):

#     tortoise = data[0]
#     hare = data[0]

#     while True:
#         tortoise = data[tortoise]
#         hare = data[data[hare]]

#         if tortoise == hare:
#             break
    

#     ptr1 = data[0]
#     ptr2 = tortoise

#     while ptr1 != ptr2:
#         ptr1 = data[ptr1]
#         ptr2 = data[ptr2]
    
#     return ptr1

    
    


# data = list(map(int, input()))
# print(find_dup(data))

# import copy

# arr = [1,2,3,4]

# def delete(arr, n):
#     arr.remove(arr[n])
    

# def dfs(arr, n):
#     if n == 3:
#         return
    
#     arr = copy.deepcopy(arr)
#     #arr.append(5)
#     delete(arr, n-1)
#     print(arr)
#     dfs(arr,n+1)

# dfs(arr,0)
# import random
# orders = [(1,3), (2,5),(3,3)]
# select = []
# select = random.sample(orders,1)
# print(select)
# x, y = select[0]
# print(f"x: {x}, y: {y}")





"""
default dictionary example
"""
# from collections import defaultdict

# trees = defaultdict(lambda :[])

# trees[(0,1)].append(3)
# trees[(0,1)].append(1)
# trees[(0,1)].append(5)

# trees[(1,1)].append(3)
# trees[(1,1)].append(1)
# trees[(1,1)].append(5)

# print(trees)

# sel_tree = trees[(0,1)]
# sel_tree.sort()

# print(sel_tree)

"""
array pending example
"""
# import copy
# arr = [[5,0,1,0],[3,2,0,1],[6,0,1,0],[0,2,0,1]]

# blue = [[0]*6 for _ in range(4)]
# for i in range(4):
#     k = 0
#     for j in range(2,6):
#         blue[i][j] = arr[i][k]
#         k += 1


# green = [[0]*4 for _ in range(6)]
# k = 0
# for i in range(2,6):
#     for j in range(4):
#         green[i][j] = arr[k][j]
        
#     k += 1

# print(blue)
# print(green)
"""
list example
"""
# info = [(2,'L'),(1,'D')]
# for command in info: 
#     (t, direction) = command
#     if 2 == t:
#         print('yes')
#         if 'L' == direction:
#             print('ok')

# t, direction = info.pop()

# print(f"{t}, {direction}")

"""
dfs example
"""
# maps = [[1,1,1],[1,0,1],[0,0,1]]
# dx = [0,0,-1,1]
# dy = [-1,1,0,0]
# cnt = 0
# def dfs(i,j):
#     global cnt
#     if i < 0 or i >= 3 or j < 0 or j >=3:
#         print("here - exit")
#         return False 
    
#     if maps[i][j] == 1:
#         maps[i][j] = -1
#         cnt += 1
#         print(maps)
#         dfs(i+1,j)
#         dfs(i-1,j)
#         dfs(i,j+1)
#         dfs(i,j-1)

#         return True
#     return False

# dfs(0,0)


# print(cnt)


# sharks = [(3,1,2),(2,4,3),(5,7,9)]
# maps = [[0]*4 for _ in range(4)]

# maps[0][1] = [(3,1,2),(2,4,3)]
# maps[2][1] = [(5,7,9)]

# for shark in sharks:
#     print('here')
#     s,d,z = shark
#     loc = 0
#     for i in range(4):
#         for j in range(4):
#             if maps[i][j] == [(s,d,z)]:
#                 loc = (i,j)
#                 break
    
#     print(loc)

# fishes = maps[0][1]
# fishes.sort()
# maps[0][1].append((5,4,3))
# print(maps)
# print('')
# fishes.sort(reverse=True, key= lambda x:x[2] )
# print(fishes)
# print('')
# maps[0][1] = fishes[0]
# print(maps)

# temp = ''
# conv_kakao = 'ab'
# temp = conv_kakao
# print(temp)
# while len(conv_kakao) != 3:
#     if len(conv_kakao) <= 2:
#         conv_kakao = conv_kakao + temp[len(temp)-1]


# print(conv_kakao)

# test = [(1,3),(2,5),(5,6)]

# x, y = 2, 5
# if (x, y) == test[1]:
    
#     print('yes')
# else:
#     print('no')

# n = int(input())

# maps = [[*map(int, input().split())] for _ in range(n)]

# print(maps)
"""
Back Tracking

"""
# ret = []
# n = 3
# def process(n, openP, closedP, Str):
#     global ret
#     if openP == n and closedP == n:
#         ret.append(Str)
#         #print(Str)
#         return 

#     if openP < n:
#         process(n, openP+1, closedP, Str+'(')

#     if openP > closedP:
#         process(n, openP, closedP+1, Str+')')
    
    


# process(n, 0, 0, '')
# print(ret)


List = [1,2,3,4]
ans = []
tmp = []
def process(index):
    #global tmp
    if index == len(List):
        print(ans)
        #tmp.append(ans)
        return 

    for i in List:
        if i in ans:
            continue
        ans.append(i)
        process(index+1)
        ans.remove(i)

#res = []
process(0)
#print(res)

