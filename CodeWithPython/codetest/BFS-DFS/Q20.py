"""
surveilance system
"""

n = int(input())

data = []
for _ in range(n):
    data.append(list(map(str, input().split())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


temp = [['X']*n for _ in range(n)] # for copying origin map

captured = 0 # number of studednts who captured
flag = False

# 3 obstacles(wall) must be existed in the map
# this problem should be solved using dfs

#surveilance function
def surveilance(x,y):

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            
            if temp[nx][ny] == 'S':
                temp[nx][ny] = 'C' #captured
                #captured += 1
                surveilance(nx, ny)
            


def dfs(cnt):

    global captured
    global flag
    
    #captured = 0

    if cnt == 3 :
        # surveilance camera
        #def check - avoidance by surveilance
        for i in range(n):
            for j in range(n):
                temp[i][j] = data[i][j]


       # print(temp)

        for i in range(n):
            for j in range(n):
                if temp[i][j] == 'T':
                    surveilance(i,j)
        
        #check map
        for i in range(n):
            for j in range(n):
                if temp[i][j] == 'C':
                    captured += 1

        if captured == 0:
            flag = True
            #print(temp, end = '\n')
            #exit(0)
        

        return     


    for i in range(n):
        for j in range(n):

            if data[i][j] == 'X':
                data[i][j] = 'O'
                cnt += 1
                dfs(cnt)
                cnt -= 1
                data[i][j] = 'X'
                    


dfs(0)

if flag:
    print('YES')
else:
    print('NO')