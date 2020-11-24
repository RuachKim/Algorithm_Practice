"""
Greedy method: find all the ways to achieve goal.
count the number of condition, includes '3' in time
"""

# n = int(input())
# cnt = 0
# for i in range(n+1):
#     for j in range(60):
#         for k in range(60):
#             num = str(i)+str(j)+str(k)
#             if '3' in num:
#                 cnt += 1
# print(cnt)


"""
Chess Board 
Find all the available location knight can move
"""

# dat = input()
# #row, col -> cur
# row = int(dat[1])
# col = int(ord(dat[0])) - ord('a') + 1

# nite_steps = [ (-1,-2), (1,-2), (-1,2), (1,2), (2,1), (2,-1), (-2,-1), (-2,1) ]

# cnt = 0
# for step in nite_steps:
#     next_row = row + step[0]
#     next_col = col + step[1]

#     if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
#         cnt += 1

# print(cnt)

"""
Game Development
move character with each direction
"""

# n, m = map(int, input().split())
# x, y, to = map(int, input().split())


# array =[]
# for i in range(n):
#     array.append(list(map(int, input().split())))

# #print(array)        

# #visited map - init with zero
# v = [[0]*m for _ in range(n)]

# v[x][y] = 1 # cur location

# dx = [-1, 0, 1, 0]
# dy = [ 0, 1, 0, -1]

# def turn_left():
#     global direction
#     direction = direction -1
#     if direction == -1:
#         direction = 3
        
# cnt = 1 #already taken by cur_character
# turn_time = 0 #turning time by 4
# direction = 0
# while True:
    
#     turn_left()
#     nx = x + dx[direction]
#     ny = y + dy[direction]
     
#     if array[nx][ny] == 0 and v[nx][ny] == 0:
#         x = nx
#         y = ny
#         cnt += 1
#         turn_time = 0
#         v[nx][ny] = 1
#         continue
#     else:
#         turn_time += 1
    
    
#     if turn_time == 4:
#         nx = x - dx[direction]
#         ny = y - dy[direction]
#         if array[nx][ny] == 0:
#             cnt += 1
#             v[nx][ny] = 1
#         else:
#             break
        
# print(cnt)
   
