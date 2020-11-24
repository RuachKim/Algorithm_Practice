from collections import deque

n, k = map(int, input().split())
q = deque(map(int, input().split()))
robot = deque([0]*2*n)

level = 1

print("#init state:")
print(f"Q: {q}")
print(f"R: {robot}")

while True:

    #1 stage
    q.rotate(1) #내구도
    robot.rotate(1)
    robot[n-1] = 0

    print(f"#level: {level}")
    print(f"Q: {q}")
    print(f"R: {robot}")
    #2 stage
    for i in range(n-2, -1, -1):
        if(robot[i] == 1 and robot[i+1] == 0 and q[i+1] > 0):
            q[i+1] -= 1
            robot[i+1] = robot[i]
            robot[i] = 0
    robot[n-1] = 0
    #3 stage
    if robot[0] == 0 and q[0] > 0:
        robot[0] = 1
        q[0] -= 1
    
    print(f"#level: {level}")
    print(f"Q: {q}")
    print(f"R: {robot}")

    cnt = 0
    for i in range(len(q)):
        if q[i] == 0:
            cnt += 1

    if cnt >= k:
        break

    level += 1

    


print(level)



