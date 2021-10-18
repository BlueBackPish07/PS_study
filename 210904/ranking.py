
def solution(n, results):
    wins, loses = {}, {}

    for i in range(1,n+1):
        wins[i], loses[i] = set(), set()

    for i in range(1, n+1):
        for battle in results:
            if battle[0] == i : # i가 이긴 사람들(루저)
                wins[i].add(battle[1])
            if battle[1] == i: # i 가 진 사람들(위너)
                loses[i].add(battle[0])

        # i에게 이긴 사람들은(winner), 자동으로 i에게 진 사람들에 비해 우위에 있다.
        # i에게 진 사람들의 정보는 wins[i] 에 있고, 반복문을 돌면서 wßinner의 승패 정보에(wins[winner]) 
        # 이 정보들을 업데이트 시켜준다. 
        for winner in loses[i]:
            wins[winner].update(wins[i])
        for loser in wins[i]:
            loses[loser].update(loses[i])
     

    cnt = 0

    for i in range(1, n+1):
        if len(wins[i])+ len(loses[i]) == n-1:
            cnt +=1
    
    return cnt

n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
print(solution(n, results))