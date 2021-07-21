from collections import deque
import sys

#
#
#
#

dy = [-1, 0, 1, 0] #포인트
dx = [0, 1, 0, -1]
n, m = map(int, input().split())
r, c, d = map(int, input().split())

# 지도
lis = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

def turn(d) :
    return (d+3)%4
def back(d) : 
    return (d+2)%4

def sol (row, col, d):
    cnt = 1 #처음 청소기 놓임
    lis[row][col] = 2 # 청소함
    q = deque([[row, col, d]])
    while q:
        row, col, d = q.popleft()
        temp_d = d #포인트
        for i in range(4):
            temp_d = turn(temp_d)
            new_row = row + dy[temp_d]
            new_col = col + dx[temp_d]
            # temp_d가 가르키는 방향으로 이동하게 된다.
            # temp_d = 0 (북) -> dy[0] = -1 , dx[0] = 0 이므로 북쪽으로 이동.
            # temp_d = 1 (동)-> dy[1] = 0 , dx[1] =  1이므로 동쪽으로 이동.
            # ect..

            if 0 <= new_row < n and 0 <= new_col < m and lis[new_row][new_col] == 0:
                cnt +=1
                lis[new_row][new_col] ==2
                q.append([new_row, new_col, temp_d])
                break
            
            elif i == 3 : #한바퀴 다 둘러봤는데 0을 만나지 못하면
                new_row = row + dy[back(d)]
                new_col = col + dx[back(d)]
                q.append([new_row, new_col, d])

                if lis[new_row][new_col] ==1 :
                    return cnt


print(sol(r, c, d))
        