import sys
import collections
import heapq

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

V, E = map(int,input().split()) # 정점 수, 간선 수
start = int(input()) # 시작 정점
graph = collections.defaultdict(list) # 빈 그래프 생성

for _ in range(E):
    u, v, w = map(int,input().split()) # (정점, 다음 정점, 가중치)
    graph[u].append((v,w)) # 그래프 생성

# 다익스트라 알고리즘
def daikstra(graph, V, start):
    # input: graph, V:정점 수, start: 시작 정점
    Q = [(0, start)] # 우선순위 큐 생성, (거리, 정점)
    distance = collections.defaultdict(int) # 거리 정보를 담을 dict 생성

    while Q: # Q가 빌때 까지 반복
        dist, node = heapq.heappop(Q) # 거리, 정점 추출
        if node not in distance: # 탐색하지 않은 node이면 탐색 진행
            distance[node] = dist # 거리 정보 갱신
            for v, w in graph[node]: # 인접 노드로 이동
                update = dist + w # 거리 정보 갱신
                heapq.heappush(Q, (update, v)) # 우선순위 큐에 삽입

    for i in range(1,V+1):
        if i == start: # 시작 정점은 거리 0 출력
            print('0')
        elif not distance[i]: # 경로가 존재하지 않은 경우
            print('INF')
        else: # 최단 경로가 존재하면
            print(distance[i])

daikstra(graph, V, start)