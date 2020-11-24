"""
Kakao question - sorting problem

    # N - total number of stage
    # stages - current stage of each player
    
    1. sort the stages
    2. calculate failure rate from the first player's stage
    3. insert the result into the list
    4. sort the list and export the label with stage 

"""

def solution(N, stages):
    answer = []

    table = []
    stages.sort()

    t_cnt = 0
    f_cnt = 0
    for i in range(1,N+1):
        for j in stages:
            if j >= i:
                t_cnt += 1
                if j == i:
                    f_cnt += 1
        
        f_rate = f_cnt/t_cnt
        table.append((i, f_rate))
        t_cnt = 0
        f_cnt = 0

    table.sort(key = lambda item: item[1], reverse= True)
    
    #print(table)
    for i,j in table:
        answer.append(i)
    
    #print(answer)
    return answer

stages = [2,1,2,6,2,4,3,3]
solution(5,stages)


