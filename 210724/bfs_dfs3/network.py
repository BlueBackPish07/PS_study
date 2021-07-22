
#https://programmers.co.kr/learn/courses/30/lessons/43162
from collections import deque
visited = list([0]*201)
def solution(n, computers):
    cnt = 0
    queue = deque()
    l = len(computers)
    for i in range(l):
        if visited[i] == 0: #미방문시
            cnt += 1 #카운트 증가
            queue.append(i) #큐에 추가
            visited[i] = 1 #방문 체크
    
        while queue:
            check = queue.popleft()
            for i in range(n):
                if computers[check][i] != 0 and i!=check: #더이상연결되지 않거나, 나 자신 외에 연결되면
                    if visited[i]==0 :
                        visited[i]=1;
                        queue.append(i)

    return cnt

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))