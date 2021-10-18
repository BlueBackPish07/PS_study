from collections import deque 

def solution(game_board, table):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    visited = [[False]* len(table) for _ in range(len(table)) ]
    q = deque()
   
    visited[0][0] = True
    q.append((0,0))
    temp=set()
    #dfs에 시뮬레이션 
    for i in range(len(table)):
        for j in range(len(table)):
            while q:
                piece = q.popleft()
                x, y = piece
                temp.update((x,y))
                if table[x][y] == 1:
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if len(table) >= nx and 0<=nx and len(table) >ny and 0<=ny and table[nx][ny]==1 and visited[nx][ny] == False:
                            q.append((nx,ny))
                            temp.update((nx,ny))
                            visited[nx][ny] == True                
                        
        
                         
    #퍼즐 회전시키면서 빈칸과 비교하기(sort 를 사용/ 돌리면서 한번이라도 맞으면 퍼즐뻄 )

    #맞으면 퍼즐크기만큼 추가

    answer = -1
    return answer



solution([[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]],[[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]])