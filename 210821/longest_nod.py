from collections import deque

#가장 먼 노드 구하기
def solution(n, edge):
    visit = [0]*(n+1)
    graph = [[]*n for _ in range(n+1)] #2차원배열로 노드를 저장

    for a,b in edge: #[a][b]와 [b][a]의 값은 같다.
        graph[a].append(b)
        graph[b].append(a)
    
    queue= deque()
    queue.append(1)
    visit[1]=1
    
    while queue:
        n = queue.popleft()
        for i in graph[n]: #graph[n] 에는 n 노드에 연결된 각 노드들이 저장되어있다.
            if visit[i] == 0:
                queue.append(i)
                visit[i] = visit[n]+1 #visit에 각 노드로 가기 위한 길이가 저장된다.
    answer= visit.count(max(visit))

    return answer
n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n,edge))
