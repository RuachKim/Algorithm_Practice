"""
make '1' 
Dynamic Programming

Bottom-Up

d[x] : 입력 값 x 가 1이 되기 위한 최소 연산 횟 수
"""

x = int(input())

d = [0]*30001

for i in range(2, x+1):

    #1을 뺄 때. 
    #1을 더하는 이유는 횟수 때문이다.
    d[i] = d[i-1] + 1

    if i%2 == 0:
        d[i] = min(d[i], d[i//2]+1)

    if i%3 == 0:
        d[i] = min(d[i], d[i//3]+1)
    
    if i%5 == 0:
        d[i] = min(d[i], d[i//5]+1)
    
print(d[i])
    
