import sys
input = sys.stdin.readline

def snake_trace(maps, snake):
    
    for trace in snake:
        x, y = trace
        maps[x][y] = 1
        
    
def draw_maps(maps):

    for i in range(n):
        for j in range(n):
            print(maps[i][j], end=' ')
        print('',end='\n')
        
    
def move(time,x,y):
    global maps
    snake = [] #사과를 먹었을 때 마지막 칸 등록
    snake.append((x,y))
    way = 3 # right
    while True:
        time += 1
        nx = x + dx[way]
        ny = y + dy[way]

        x = nx
        y = ny
        
        
        print(f"{time} - current: {x}, {y} / snake = {snake}")
        draw_maps(maps)
        if x < 0 or x >= n or y < 0 or y >= n:
            return time

        elif maps[x][y] == 1:
            #print(f"snake = {snake}")
            print(f"collision - {x},{y}")
            return time
        
        else: 

            if maps[x][y] == '.': #apple
                #maps[x][y] = 0
                snake.insert(0, (x,y)) #register visited axis    

            elif maps[x][y] == 0:
                snake.insert(0, (x,y))
                i, j = snake.pop()
                maps[i][j] = 0
                

            for command in snake_dir:
                (t, direction) = command
                #print(f"t, direction = {t}, {direction}")
                if time == int(t):
                    print(f"here - {direction}, {way}")
                    if direction == 'D':
                        way -= 1
                    #    print(f"here - {direction}, {way}")
                    elif direction == 'L':
                        way += 1
        snake_trace(maps,snake)



if __name__ == "__main__":
    
    n = int(input())
    k = int(input())
    maps = [[0]*n for _ in range(n)] #map for snake

    apple = []
    for _ in range(k):
        x, y = map(int, input().split())
        maps[x-1][y-1] = '.'
        apple.append((x-1,y-1))


    snake_dir = []
    l = int(input())
    for _ in range(l):
        time, direction = input().split()
        snake_dir.append((time, direction))

    #up, left, down, right
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]


    time = move(0,0,0)
    print(time)

