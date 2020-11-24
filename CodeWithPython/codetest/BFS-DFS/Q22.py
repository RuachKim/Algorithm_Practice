from collections import deque

def get_next_pos(pos, board):
    
    n_pos = []
    pos = list(pos)
    pos1_x, pos1_y, pos2_x, pos2_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    for i in range(4):
        n_pos1_x, n_pos1_y, n_pos2_x, n_pos2_y = pos1_x + dx[i], pos1_y + dy[i], pos2_x + dx[i], pos2_y + dy[i]

        if board[n_pos1_x][n_pos1_y] == 0 and board[n_pos2_x][n_pos2_y] == 0:
            n_pos.append({(n_pos1_x, n_pos1_y), (n_pos2_x, n_pos2_y)})
        
    #rotation // side by side - robot
    if pos1_x == pos2_x:
        for i in [-1,1]:
            if board[pos1_x+i][pos1_y] == 0 and board[pos2_x+i][pos2_y] == 0:
                n_pos.append({(pos1_x, pos1_y), (pos1_x+i, pos1_y)})
                n_pos.append({(pos2_x, pos2_y), (pos2_x+i, pos2_y)})

    elif pos1_y == pos2_y:
        for i in [-1,1]:
            if board[pos1_x][pos1_y+i] == 0 and board[pos2_x][pos2_y+i] == 0:
                n_pos.append({(pos1_x, pos1_y), (pos1_x, pos1_y+i)})
                n_pos.append({(pos2_x, pos2_y), (pos2_x, pos2_y+i)})

    return n_pos       
        

# BFS
def solution(board): 
    
    n = len(board)
    n_board = [[1]*(n+2) for _ in range(n+2)]

    for i in range(n):
        for j in range(n):
            n_board[i+1][j+1] = board[i][j]
            
    q = deque()
    pos = {(1,1),(1,2)}
    cost = 0
    q.append((pos, cost))
    visited = []
    visited.append(pos)
    
    while q:
        
        pos, cost = q.popleft()
        
        if (n,n) in pos:
            return cost
        
        for n_pos in get_next_pos(pos, n_board):
            if n_pos not in visited:
                q.append((n_pos, cost+1))
                visited.append(n_pos)
    
    return 0

board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
print(solution(board))