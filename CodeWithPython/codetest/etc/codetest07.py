"""
binary search with multiple-items
"""

# n = int(input())
# a = list(map(int, input().split()))
# a.sort()
# #print(a)

# m = int(input())
# b = list(map(int, input().split()))

# def binSearch(start, end, target):

#     if start > end:
#         return False
    
#     mid = (start+end)//2

#     if a[mid] == target:
#         return True
#     elif a[mid] < target:
#         return binSearch(mid+1, end, target)
#     else:
#         return binSearch(start, mid-1, target)

# for item in b:

#     res = binSearch(0, n-1, item)
#     if res == True:
#         print('Yes', end=' ')
#     else:
#         print('No', end=' ')

"""
Rice cake - How long is the size of cutter for slicing rice cake.

But This method is way overweighed to calcuate if the incoming number is greater than billions.. 
"""

#n, m = map(int, input().split())

# a = [19, 15, 10, 17]
# mx = max(a)
# sum = 0
# temp = []
# for i in range(mx, 0, -1):
#     for j in a:
#         if i <= j:
            
#             sum += (j - i)
#             print(f'rice: {j}, cutter: {i}, sum: {sum}')
#             #print(sum, end = ' ')

#     if sum == 6:
#         temp.append(i)
#         break       
#     sum = 0

# print(temp)


"""
To find the answer easiear, we can use BinarySearch.
But Recursion way will be much more difficult, so here we write the code using "while" repetition.
"""

n, target = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)

ans = 0
sum = 0

while start <= end:

    mid = (start+end)//2
   
    for i in array:
        if i >= mid:
            diff = i - mid
            sum += diff

    if sum > target:
        start = mid + 1
    
    elif sum < target:
        end = mid - 1
    
    else :
        ans = mid
        break
    
    sum = 0
    

print(ans)
