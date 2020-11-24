from collections import deque


def rotate(direction, tiles):
    if direction == '+':

        turn = tiles.pop()
        tiles.appendleft(turn)
    
    elif direction == '-':
        
        turn = tiles.popleft()
        tiles.append(turn)

    return tiles

F = ['r'*3 for _ in range(3)]
B = ['o'*3 for _ in range(3)]
L = ['g'*3 for _ in range(3)]
R = ['b'*3 for _ in range(3)]
U = ['w'*3 for _ in range(3)]
D = ['y'*3 for _ in range(3)]

numoftc = int(input())

step = deque()
tiles = deque()
cnt = 1
while numoftc:
    
    tc = int(input())
    
    step = input().split()
    print(step)
    step.reverse()
    
    
    while step:
        c = step.pop()
        surface = c[0]
        direction = c[1]

        print(f'surface = {surface}; direction = {direction}')

        #manipulation tile from the axis of each surfaces
        

        if surface == 'F':
            #initialization of tiles
            tiles.append(U[2])
            tiles.append((R[0][0]+R[1][0]+R[2][0]))
            tiles.append(D[2])
            tiles.append((L[0][2]+L[1][2]+L[2][2]))

            #rotate tiles +/-
            tiles = rotate(direction, tiles)

            U[2] = tiles[0]
            R[0] = tiles[1][0] + R[0][1] + R[0][2]
            R[1] = tiles[1][1] + R[1][1] + R[1][2]
            R[2] = tiles[1][2] + R[2][1] + R[2][2]
            D[2] = tiles[2]
            L[0] = L[0][0] + L[0][1] + tiles[3][0]
            L[1] = L[1][0] + L[1][1] + tiles[3][1]
            L[2] = L[2][0] + L[2][1] + tiles[3][2]
            
            tiles.clear()
        
        elif surface == 'B':
            #initialization of tiles
            tiles.append(U[0])
            tiles.append((L[0][0]+L[1][0]+L[2][0]))
            tiles.append(D[0])
            tiles.append((R[0][2]+R[1][2]+R[2][2]))

            #rotate tiles +/-
            tiles = rotate(direction, tiles)

            U[0] = tiles[0]
            L[0] = tiles[1][0] + L[0][1] + L[0][2]
            L[1] = tiles[1][1] + L[1][1] + L[1][2]
            L[2] = tiles[1][2] + L[2][1] + L[2][2]
            D[0] = tiles[2]
            R[0] = R[0][0] + R[0][1] + tiles[3][0]
            R[1] = R[1][0] + R[1][1] + tiles[3][1]
            R[2] = R[2][0] + R[2][1] + tiles[3][2]
            
            
            tiles.clear()
        
        elif surface == 'L':
            #initialization of tiles
            tiles.append((U[0][0]+U[1][0]+U[2][0]))
            tiles.append((F[0][0]+F[1][0]+F[2][0]))
            tiles.append((D[0][2]+D[1][2]+D[2][2]))
            tiles.append((B[0][2]+B[1][2]+B[2][2]))

            #print(tiles)
            #rotate tiles +/-
            tiles = rotate(direction, tiles)

            #print(tiles)

            U[0] = tiles[0][2] + U[0][1] + U[0][2]
            U[1] = tiles[0][1] + U[1][1] + U[1][2]
            U[2] = tiles[0][0] + U[2][1] + U[2][2]

            F[0] = tiles[1][0] + F[0][1] + F[0][2]
            F[1] = tiles[1][1] + F[1][1] + F[1][2]
            F[2] = tiles[1][2] + F[2][1] + F[2][2]

            D[0] = D[0][0] + D[0][1] + tiles[2][2]
            D[1] = D[1][0] + D[1][1] + tiles[2][1]
            D[2] = D[2][0] + D[2][1] + tiles[2][0]

            B[0] = B[0][0] + B[0][1] + tiles[3][0]
            B[1] = B[1][0] + B[0][1] + tiles[3][1]
            B[2] = B[2][0] + B[0][1] + tiles[3][2]

            #print(tiles)
            
            tiles.clear()


        elif surface == 'R':
             #initialization of tiles
            tiles.append((U[0][2]+U[1][2]+U[2][2]))
            tiles.append((B[0][0]+B[1][0]+B[2][0]))
            tiles.append((D[0][0]+D[1][0]+D[2][0]))
            tiles.append((F[0][2]+F[1][2]+F[2][2]))
            
            #print(tiles)

            #rotate tiles +/-
            tiles = rotate(direction, tiles)

            #print(tiles)

            U[0] = U[0][0] + U[0][1] + tiles[0][0]
            U[1] = U[1][0] + U[1][1] + tiles[0][1]
            U[2] = U[2][0] + U[2][1] + tiles[0][2]

            B[0] = tiles[1][2] + B[0][1] + B[0][2] 
            B[1] = tiles[1][1] + B[1][1] + B[1][2]
            B[2] = tiles[1][0] + B[2][1] + B[2][2]

            D[0] = tiles[2][0] + D[0][1] + D[0][2]
            D[1] = tiles[2][1] + D[1][1] + D[1][2]
            D[2] = tiles[2][2] + D[2][1] + D[2][2]

            F[0] = F[0][0] + F[0][1] + tiles[3][2]
            F[1] = F[1][0] + F[1][1] + tiles[3][1]
            F[2] = F[2][0] + F[2][1] + tiles[3][0]
            
            
            
            tiles.clear()


        elif surface == 'U':
             #initialization of tiles
            tiles.append(B[0])
            tiles.append(R[0])
            tiles.append(F[0])
            tiles.append(L[0])

            #print(tiles)

            #rotate tiles +/-
            tiles = rotate(direction, tiles)

            #print(tiles)

            B[0] = tiles[0]
            R[0] = tiles[1]
            F[0] = tiles[2]
            L[0] = tiles[3]

        
            tiles.clear()

        elif surface == 'D':
             #initialization of tiles
            tiles.append(B[2])
            tiles.append(L[2])
            tiles.append(F[2])
            tiles.append(R[2])

            #print(tiles)

            #rotate tiles +/-
            tiles = rotate(direction, tiles)

            #print(tiles)

            B[2] = tiles[0]
            L[2] = tiles[1]
            F[2] = tiles[2]
            R[2] = tiles[3]

        
            tiles.clear()

        print(f"{cnt} stage")
        print(f'U:{U}')
        print(f'F:{F}')
        print(f'D:{D}')
        print(f'B:{B}')
        print(f'L:{L}')
        print(f'R:{R}')

        cnt += 1
        


    numoftc -= 1

# print(f'U:{U}')
# print(f'F:{F}')
# print(f'D:{D}')
# print(f'B:{B}')
# print(f'L:{L}')
# print(f'R:{R}')