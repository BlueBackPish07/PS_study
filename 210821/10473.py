import math
import heapq
import sys
inf = math.inf

# start = [23.0, 100.0]
# end = [190.0, 57.5]
# n = 4
# nodes = [ [125.0, 67.5],
#         [75.0, 125.0],
#         [45.0, 72.5],
#         [185.0, 102.5]
# ]

def getDis(start, next): 
    cx = start[0]
    cy = start[1]
    nx= next[0]
    ny= next[1]
    dis = ((cx-nx)**2 + (cy-ny)**2) ** 0.5
    return dis

def sol(start, grp):
    visited = [[inf]* n for _ in range(n)]
    visited[start] = 0
    heap = []
    heapq.heappush(heap, [0,start]) 
    #첫번째 요소를 기준으로 정렬한다.
    ###막힘!

    return 0  

startx, starty = map(float, sys.stdin.readline().split())
endx, endy = map(float, sys.stdin.readline().split())
n = int(input())

arr = [[]for _ in range(n+2)]
arr[0] = (startx, starty)
for i in range(1,n):
    x, y = map(float, sys.stdin.readline().split())
    arr[i] = [x,y]
arr[n+1] = (endx, endy)

time =[[] for _ in range(len(arr))]
for i in range(len(arr)):
    for j in range(len(arr)):
        if i == 0 or i == len(arr)-1 : #첫번째와 마지막은 걸어가야함
            time[i].append((getDis(arr[i], arr[j]))/5)
        else: #중간노드들은 대포1번 + 걸어가야함
            time[i].append(abs(getDis(arr[i], arr[j])-50)/5 +2 )

ans = sol(0, time)