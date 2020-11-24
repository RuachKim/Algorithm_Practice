"""
upgly number
"""

n = int(input())

ugly = [0]*n
nxt2, nxt3, nxt5 = 2,3,5 #init number

ugly[0] = 1

i2, i3, i5 = 0, 0, 0

for l in range(1,n):

    ugly[l] = min(nxt2, nxt3, nxt5)

    if ugly[l] == nxt2:
        i2 += 1
        nxt2 = ugly[i2]*2
    
    if ugly[l] == nxt3:
        i3 += 1
        nxt3 = ugly[i3]*3
    
    if ugly[l] == nxt5:
        i5 += 1
        nxt5 = ugly[i5]*5

print(ugly[n-1])