
array = [9, 6, 5, 3, 1, 5, 6, 3, 2, 10, 11, 7, 20, 13, 12, 12, 4, 8, 10]

""""
selection sort
normally O(N^2)
"""

# for i in range(len(array)):
#     min_indx = i
#     for j in range(i+1, len(array)):
#         if array[j] < array[min_indx]:
#             min_indx = j
    
#     array[min_indx], array[i] = array[i], array[min_indx]
    

# print(array)


"""
insertion sort
normally,  O(N^2), especially short when array already be sorted, O(N)
"""

# for i in range(1, len(array)):
#     for j in range(i, 0, -1):
#         if array[j] < array[j-1]:
#             array[j], array[j-1] = array[j-1], array[j]
#         else:
#             break


# print(array)




"""
Quick sort
populary used - So fast

pivot!

O(NlogN) - normal state 
O(N^2) - for bad condition
"""

# def Quick(start, end, array):
#     if start >= end:
#         return
    
#     pivot = start
#     left = start + 1
#     right = end

#     while left <= right:
#         while left <= end and array[left] <= array[pivot]:
#             left += 1
        
#         while right > start and array[right] >= array[pivot]:
#             right -= 1

#         if left > right:
#             array[right], array[pivot] = array[pivot], array[right]
#         else:
#             array[left], array[right] = array[right], array[left]

#     Quick(start, right-1, array)
#     Quick(right+1, end, array)



# Quick(0, len(array)-1, array)
# print(array)




def Quick_p(array):

    if len(array) <= 1:
        return array
    
    pivot = array[0]
    tail = array[1:]

    left = [x for x in tail if x <= pivot]
    right = [y for y in tail if y > pivot]

    return Quick_p(left) + [pivot] + Quick_p(right)

print(Quick_p(array))


