from collections import deque
import sys

input = sys.stdin.readline


def search(shark):
    s,d,z = shark
    global loc
    exist = False
    for i in range(R):
        for j in range(C):
            if maps[i][j] == [(s,d,z)]:
                loc = (i,j)
                exist = True
                break

    if exist:
        return True

    return False


def fight():

    for i in range(R):
        for j in range(C):
            if len(maps[i][j]) > 1: # 1마리 이상
                fishes = maps[i][j]
                fishes.sort(reverse=True, key=lambda x:x[2])
                maps[i][j] = fishes[0]
                for i in range(len(fishes)):
                    if i > 0:
                        sharks.remove(fishes[i])
                
                        

def move_shark():

    for shark in sharks:
        s, d, z = shark
        speed = sprincesa12
        
        x, y = 0, 0
        if search(shark):
            (x, y) = loc
        else:
            continue

        step = 1
        maps[x][y].clear()
        
        while step <= speed and (x >= 0 and y >= 0 and x < R and y < C):
            if step == 1:
                nx = x + dx[d-1]
                ny = y + dy[d-1]

            if x > 0 and y > 0 and x < (R-1) and y < (C-1):
                nx = x + dx[d-1]
                ny = y + dy[d-1]
            
            else:
                nx = x - dx[d-1]
                ny = y - dy[d-1]
            
            x, y = nx, ny 
            step += 1       
        
        maps[x][y].append((s,d,z))


def fishing():

    index = 0

    while True:
        
        #game over
        if index == C-1:
            return  

        catched = False
        for i in range(R):
            #shark been found!
            if not maps[i][index] == 0:
                catch.append(maps[i][index])
                maps[i][index] = 0
                catched = True
                break
        
        
        #def move shark
        move_shark()
        fight()

        index += 1


            

if __name__ == "__main__":
    
    R,C,m = map(int, input().split())
    loc = 0
    maps = [[0]*C for _ in range(R)]
    sharks = []
    for _ in range(m):
        r,c,s,d,z = map(int, input().split())
        maps[r-1][c-1] = [(s,d,z)]
        sharks.append((s,d,z))
    catch = []
    #up down right left
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]

    fishing()

    print(catch)


