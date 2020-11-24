#Greedy (Dynamic Programming) - Easy
# Great sum with Great number
# N, M, K is given and list of N is given
# each arg means Number of input, number of sum, minimal sum of number in same index

# n, m, k = map(int, input().split())
# dat = list(map(int, input().split()))

# dat.sort()

# Max_first = dat[n-1]
# Max_sec = dat[n-2]

# # print(dat)
# # print(Max_first,Max_sec)

# sum = 0

# # while True:
# #     for i in range(k):
# #         if m == 0:
# #             break
        
# #         sum += Max_first
# #         m = m-1
    
# #     if m == 0:
# #         break
# #     sum += Max_sec

# #     m = m-1


# # print(sum)

# a_cnt = m//k*k
# b_cnt = m%k
# sum = a_cnt*dat[n-1] + b_cnt*dat[n-2]

# print(sum)

#Greedy (Dynamic Programming) - Easy
#Number Card Game - Select great number among the numbers in each rows

# n,m = map(int, input().split())
# max = 0
# for i in range(n):
#     data = list(map(int, input().split()))
#     data.sort()
    
#     if max < data[0]:
#         max = data[0]

# print(max)

# n, k = map(int, input().split())
# cnt = 0
# while n != 1:
#     if n%k == 0:
#         n = n/k
#     else:
#         n = n-1
#     cnt+=1

# print(cnt)

#Implement (Basic)
#L R U D
#input : n x n dimensional matrix, Direction

n = int(input())
print(n)
Dir = list(map(str, input().split()))
#print(Dir)
cur_x = 1
cur_y = 1

for i in Dir:
    if i == 'R':
        if cur_y < n:
            cur_y += 1
        
    elif i == 'L': 
        if cur_y > 1:
            cur_y -= 1

    elif i == 'U':
        if cur_x > 1:
            cur_x -= 1
    elif i == 'D':
        if cur_x < n:
            cur_x += 1
print(cur_x,cur_y)
    




