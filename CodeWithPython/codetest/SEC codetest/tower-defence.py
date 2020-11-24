import sys
import copy
from itertools import combinations
from collections import deque

input = sys.stdin.readline

def calc_dist(attacker, opponents):

    min_value = int(1e9)
    x, y = attacker
    targets = [] 
    for opponent in opponents:
        x1, y1, cnt = opponent
        dist = abs(x-x1) + abs(y-y1)
        targets.append((x1,y1,dist))
    
    targets.sort(key = lambda x:x[2])
    
    
    return targets[0]

def war():
    
    #radar_maps = copy.deepcopy(maps)

    while True:
        
        print(f"enemy info: {enemies}")

        for attacker in archery:
            
            #target selected
            target = calc_dist(attacker, enemies)
            x1, y1, dist = target
            for opponent in enemies:
                x, y, cnt = opponent 
                if x1 == x and  y1 == y:
                    opponent[2] += 1 
        
        #화살 맞은 적 제거 or 성 침투한 적
        global enemies_killed
        isFind = False
        while True:
            for opponent in copy.deepcopy(enemies):
                #enemies
                if opponent[2] > 0:
                    enemies.remove(opponent)
                    enemies_killed += 1
                    isFind = True
                if opponent[0] >= n:
                    enemies.remove(opponent)
                    isFind = True
            if isFind == False:
                break
            else:
                isFind = False
       
       
        #check the end condition
        
        if len(enemies) == 0: #no enemies
            return enemies_killed

        

        #update enemies location
        for opponent in enemies:
            opponent[0] += 1



if __name__ == "__main__":
    
    n, m, d = map(int, input().split())

    maps = []
    for _ in range(n):
        maps.append(list(map(int, input().split())))

    castle = [ i for i in range(m)]
    
    all_case = combinations(castle,3)

    archery = deque()
    enemies = deque()
    
    enemies_killed = 0
    

    for case in all_case:

        #Init
        #Enemies location stored
        cnt = 0
        for i in range(n):
            for j in range(m):
                if maps[i][j] == 1:
                    enemies.append([i,j,cnt])
        
        #Archery location stored
        for i in case:
            archery.append([n,i])

        #WAR routine working 
        war()

        print(f"archery = {archery}")
        print(f"enemies = {enemies}")
        print(f"killed = {enemies_killed}")
        archery.clear()
        enemies.clear()


