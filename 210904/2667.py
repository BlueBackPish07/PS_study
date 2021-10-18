import sys
dx=[-1,0,1,0]
dy=[0,1,0,-1]
n=int(sys.stdin.readline())
a=[list(sys.stdin.readline()) for _ in range(n)]
cnt=0 
apt=[]

def dfs(x,y):
    global cnt
    a[x][y] = '0' #방문한 곳은 0으로
    cnt+=1 #아파트 갯수를 카운트
    for i in range(4): # 상하좌우 탐색
        nx = x + dx[i] 
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >=n: # 범위내일때는 무시
            continue
        if a[nx][ny] == '1': #아파트 있을때 재귀
            dfs(nx,ny)

for i in range(n):
    for j in range(n):
        if a[i][j] == '1':
            cnt= 0
            dfs(i,j)
            apt.append(cnt) #아파트 단지 정보를(아파트 갯수) 저장한다.

print(len(apt)) #단지 갯수
apt.sort() # 내림차순 정렬
for i in apt:
    print(i)