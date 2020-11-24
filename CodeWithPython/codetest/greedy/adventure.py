"""
there are N people, those people, each has an fear-level that means they need at least those 
number of members as much as fear-level to achieve the goal.
How many groups can be made up?

var
count : people in group
result : answer (Group)
"""

# num = int(input())
# inputs = list(map(int, input().split()))

# inputs.sort()
# cnt = 0
# result = 0

# for i in inputs:
#     cnt += 1
#     if cnt >= i:
#         cnt = 0
#         result += 1

# print(result)




"""
+/* operation, pp312
"""
# number = list(map(int, input().split()))

# result = number[0]

# for i in range(1, len(number)):
#     if number[i] <= 1 or result <= 1:
#         result += number[i]
#     else:
#         result *= number[i]

# print(result)



"""
Binary inversion. (1st version, heuristic version)
"""

# number = list(map(int, input()))

# cnt0 = 0
# cnt1 = 0
# flag_0 = False
# flag_1 = False

# for i in number:
#     if i == 0:
#         cnt0 += 1
        
#         flag_1 = False

#         if flag_0:
#             cnt0 -= 1
#             #flag_0 = False 
#         else:
#             flag_0 = True

#     elif i == 1:
#         cnt1 += 1
#         flag_0 = False

#         if flag_1:
#             cnt1 -= 1
#             #flag_1 = False
#         else:
#             flag_1 = True


# print(f"cnt0 = {cnt0}, cnt1 = {cnt1}")

# if cnt0 < cnt1: 
#     print(cnt0)
# else:
#     print(cnt1)

"""
Binary inversion. (2nd version, smart version)
"""

numb = list(map(int, input()))
cnt0 = 0 # number of switching 0
cnt1 = 0 # number of switching 1

if numb[0] == 1:
    cnt0 += 1
else:
    cnt1 += 1


for i in range(len(numb)-1):
    if numb[i] != numb[i+1]:

        if numb[i+1] == 1:
            cnt0 += 1
        else:
            cnt1 += 1

print(min(cnt0,cnt1))
