import copy as cp

def dfs(index):
    global arr
    if index == len(position):
        #calculation minimum space(width)
        return

    else:

        temp = cp.deepcopy(arr)
        version, x, y = position[index]

        if version == 1:
            #up
            for i in range(x-1,-1,-1):
                if arr[i][y] == 0:
                    arr[i][y] = '#'
                elif arr[i][y] == 6:
                    break
            
            dfs(index+1)
            #down
            arr = cp.deepcopy(temp)
            for i in range(x+1,n):
                if arr[i][y] == 0:
                    arr[i][y] = '#'
                elif arr[i][y] == 6:
                    break
            





if __name__ == '__main__':
    
    #search cctv position and version

    n, m = map(int, input().split())
    arr = []
    position = []

    arr = [list(map(int, input().split())) for _ in range(n)]

    for i in range(n):    
        for j in range(m):
             if not (arr[i][j] == 0 or arr[i][j] == 6):
                position.append((arr[i][j],i,j))  

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]


    min_area = int(1e9)
    dfs(0)

    print(min_area)
    print(arr)

    