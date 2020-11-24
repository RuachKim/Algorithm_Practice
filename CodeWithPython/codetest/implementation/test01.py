"""
Binary search
"""

def binary_search(element, target, start, end):

    while start <= end:
        mid = (start+end)//2

        if element[mid] == target:
            return mid
        
        elif element[mid] > target:
            end = mid - 1

        else:
            start = mid + 1

    return None


n = int(input())
element = list(map(int, input().split()))

m = int(input())
search = list(map(int, input().split()))

for i in search:
    if binary_search(element, i, 0, len(element)-1):
        print('yes')
    else:
        print('no')


