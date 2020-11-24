"""
무빙워크

-무빙워크 동작 (1칸) 시작.
   - If 첫번째 타일 강도 > 0:
      -사람 투입(q[0][1] = True)
      -타일강도 1줄임(q[0][0] -= 1)

   #첫번째 칸 제외한 사람 한명씩 움직임
(마지막 사람부터)
    for tile in range(n-1, 0,-1):
        If q[tile][1] :
            If tile == n-1:
                q[tile][1] = 0
            If not q[tile+1][1] :
                  q[tile+1][1] = 1
                if q[tile+1][0] > 0:
                    q[tile+1][0] -= 1
                    q[tile][1] = 0

          Else:
                Continue


5 4
5 1 2 5 1 2 4 4 2 1

Output: 6

5 10
5 1 2 5 1 2 4 4 2 1

Output: 48???
"""

from collections import deque

def process():

    q = deque()
    for i in mov_walk:
        q.append([i,0])
    
    
    broken = 0

    while True:
        
        global time
        if broken >= m:
            return
            
        rotation = q.pop()
        q.appendleft(rotation)
        

        if q[0][0] > 0:
            q[0][1] = 1
            q[0][0] -= 1

        for tile in range(n-2, 0, -1):
            if q[tile][1] :
                
                if tile == n-2:
                    continue

                else:
                    if not q[tile+1][1] and q[tile+1][0] > 0:
                        q[tile][1] = 0
                        q[tile+1][1] = 1  
                        q[tile+1][0] -= 1

                
        q[n-1][1] = 0
        if(q[n-1][0] > 0):
            q[n-1][0] -= 1
        

        broken = 0
        for i in range(2*n):
            if q[i][0] < 1:
                broken += 1

        time += 1
        print(f"#time:{time} broken:{broken}, moving walk: {q} ")
        





tc = int(input())

for t in range(tc):
    #mov_walk = []\
    time = int(0)
    n, m = map(int, input().split())
    mov_walk = list(map(int, input().split()))

    process()
    print(time)

