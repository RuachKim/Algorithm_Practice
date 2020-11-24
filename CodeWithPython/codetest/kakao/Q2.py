from itertools import combinations

#orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
orders = ["ABCFG", "AC", "CDE"]
course = [2,3]
combos_candid = [[] for _ in range(max(course)+1)]

def solution(orders, course):
    answer = []
    combos = []
    customers = len(orders)
    
    
    for dishes in orders:

        for num in course:
            for combo in combinations(dishes, num):
                combos.append(combo)

         
    #print(combos)
    
    for combo in combos:
        guest = 0
        for dishes in orders:

            cnt = 0
            find = False
            l = len(combo)
            d = len(dishes)
            for i in range(l):
                if combo[i] in dishes:
                    cnt += 1
            
            if cnt == l:
                find = True

            if find:
                combo = "".join(combo)
                combos_candid[l].append((combo,guest))

            guest += 1
        



    return answer



solution(orders, course)
print(combos_candid)
