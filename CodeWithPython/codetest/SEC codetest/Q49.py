"""
youth shark
- DFS
"""
import copy

radar = [[None]*4 for _ in range(4)]
for i in range(4):
    data = list(map(int, input().split()))
    for j in range(4):
        radar[i][j] = [data[2*j], data[2*j+1]-1]

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]

def find_fish(arr, index):
    x, y = 0, 0
    for i in range(4):
        for j in range(4):
            if arr[i][j][0] == index:
                x, y = i, j
                return (x, y)

    return None

def change_dir(direction):
    return (direction + 1) % 8

    

def move_fish(arr, now_x, now_y):

    for k in range(1,17):
        position = find_fish(arr, k)
        if position != None:
            x, y = position[0], position[1]
            direction = arr[x][y][1]

            for i in range(8):
                nx = x + dx[direction]
                ny = y + dy[direction]

                if 0 <= nx and nx < 4 and ny >= 0 and ny < 4:
                    #상어를 안만날때
                    if not(nx == now_x and ny == now_y):
                        arr[x][y][1] = direction
                        arr[x][y], arr[nx][ny] = arr[nx][ny], arr[x][y]
                        break
                   
                direction = change_dir(direction)

    
def get_eatable_fish(arr, now_x, now_y):
    positions = []
    direction = arr[now_x][now_y][1]

    for i in range(4):
        now_x += dx[direction]
        now_y += dy[direction]

        if now_x >= 0 and now_x < 4 and now_y >= 0 and now_y < 4:
            if arr[now_x][now_y][0] != -1:
                positions.append((now_x, now_y))
    
    return positions

result = 0
def dfs(arr, now_x, now_y, total):
    global result

    narr = copy.deepcopy(arr)
    

    
    total += narr[now_x][now_y][0]
    narr[now_x][now_y][0] = -1

    move_fish(narr, now_x, now_y)
    positions = get_eatable_fish(narr, now_x, now_y)

    print(f"arr:{arr}", end = '\n')
    print('\n')
    print(narr, end = '\n')
    print('\n')

    if len(positions) == 0:
        result = max(result, total)
        return
    
    
    for nx, ny in positions:
        dfs(narr, nx, ny, total)

dfs(radar, 0, 0, 0)

print(result)




