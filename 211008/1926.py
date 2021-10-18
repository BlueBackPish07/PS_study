import sys 
from collections import deque

def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    size = 1
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0<=ny<m and 0<=nx<n :
                if arr[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append([nx,ny])
                    size +=1
    return size



n, m = map(int, sys.stdin.readline().split())
visited = [[False] * m for _ in range(n)]
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dx = [0,0,-1,1]
dy = [1,-1,0,0]

cnt = 0
max_size=0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and visited[i][j]== False:
            cnt +=1
            max_size = max(max_size, bfs(i,j))

print(cnt)
print(max_size)

    


