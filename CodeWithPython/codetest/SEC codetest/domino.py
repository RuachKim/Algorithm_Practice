"""
Domino - Tetris

Simulation
"""

import copy


def push_back():

    #끝까지 밀어버릴때.(우측 - 블루)

    for i in range(4):
        for j in range(5):
            cp_image[i][j+1] = cp_image[i][j]
            cp_image[i][j] = 0

    #끝까지 밀어버릴때.(하측 - 그린)

    for i in range(6):
        for j in range(3):
            cp_image[i][j+1] = cp_image[i][j]
            cp_image[i][j] = 0



    return

def push_one():

    #한 칸만 밀어버릴때.(우측 - 블루)
    temp = []
    for i in range(n):
        temp.clear()
        for j in range(n-1):
            if j == 0:
                #temp[0] = arr[i][1]
                temp.append(arr[i][1])
                arr[i][1] = arr[i][0]
                arr[i][0] = 0
            else:
                #temp[j] = arr[i][j+1]
                temp.append(arr[i][j+1])
                arr[i][j+1] = temp[j-1]

    #한 칸만 밀어버릴때.(하측 - 그린)

    

    return

if __name__ == "__main__":

    arr = [[0]*(4) for _ in range(4)]
    #arr = [[5,0,1,0],[3,2,0,1],[6,0,1,0],[0,2,0,1]]

    #copy to blue / green

    blue = [[0]*6 for _ in range(4)]
    green = [[0]*4 for _ in range(6)]
           
    N = int(input())

    for _ in range(N):
        t, x, y = map(int, input().split())

        #deploy block
        if t == 1:
            arr[x][y] = 1

        elif t == 2:
            arr[x][y] = 1
            arr[x][y+1] = 1

        elif t == 3:
            arr[x][y] = 1
            arr[x+1][y] = 1


        

    

