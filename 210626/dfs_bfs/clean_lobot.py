# https://www.acmicpc.net/problem/14503

import sys

n, m = map(int, input().split())
x, y, d = map(int, input().split())
lis = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
answer = 0


 # 0. 북쪽 일 경우 (-1, 0) 이동
 # 1. 동쪽일 경우 (0, 1) 이동
 # 2. 남쪽일 경우 (1, 0) 이동
 # 3. 서쪽일 경우 (0, -1) 이동 
dx = [-1,0,1,0]
dy = [0,1,0,-1]

while True:
    clean = False
    if not visited[x][y]:
        answer += 1
        visited[x][y] = True
    # 탐색
    for i in range(4):
        #뱡향 전환
        nd = (d + 3) % 4 
        #이동
        nx = x + dx[nd] 
        ny = y + dy[nd]
        d = nd 
        # 이동중 0을 만나면 청소한다.
        if not visited[nx][ny] and lis[nx][ny] ==0:
            clean = True
            x, y= nx, ny
            break
    #후진하기   
    if not clean:
        if lis[x - dx[d]][y - dy[d]] == 1:# 뒤로 이동했는데 벽이면 종료
            break
        else:
            x, y = x - dx[d], y - dy[d] # 후진한다. 


# n = 3
# m = 3 
# x = 1
# y = 1
# d = 0
# lis = [ [1,1,1],
#         [1,0,1],
#         [1,1,1]
# ]
print(answer)
            





