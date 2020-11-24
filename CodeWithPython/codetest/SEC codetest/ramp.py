from collections import defaultdict
import sys

input = sys.stdin.readline

n, l = map(int, input().split())

road = defaultdict(lambda : [])
pass_road = []
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if i == 0:
            road[(-1,0)].append(arr[i][j])
            road[(0,-1)].append(arr[j][i])
        else:    
            road[(i,0)].append(arr[i][j])
            road[(0,i)].append(arr[j][i])


#install ramp
def install_ramp(event, row):
    global pass_road
    check = False
    cnt = 0
    for i in event:
        # for step in range(1,l+1):
        #     if (i+step) < n: 
        #         if row[i] == row[i+step]:
        #             check = True
        #         else:
        #             check = False
        # if check:
        #     cnt += 1
        for step in range(l):
            while (i-step) > -1 or (i+step) < n:
                


    if cnt == len(event):
        pass_road.append(row)
        return True

    return False


#x-axis check
def x_axis_check():

    event = []
    for i in range(n):
        if i == 0:
            i = -1
        for j in range(n-1):
            row = road[(i,0)]
            if abs(row[j] - row[j+1]) == 1:

                event.append(j+1)
                
        if len(event) > 0:        
            res = install_ramp(event, row)
    


#y-axis check
def y_axis_check():

    event = []
    for i in range(n):
        if i == 0:
            i = -1
        for j in range(n-1):
            collumn = road[(0,i)]
            if abs(collumn[j] - collumn[j+1]) == 1:
                event.append(j+1)
                
        if len(event) > 0:         
            res = install_ramp(event, collumn)



x_axis_check()
#y_axis_check()

print(pass_road)