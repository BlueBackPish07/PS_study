
import collections
import sys
from collections import deque

N = 0
M = 0
map = []
vist = [[0]*N for _ in range(N)]
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

clouds = deque()
def inputMap() :
    N, M = map(int, input().split())
    for i in range(N):
        for j in range(N):
            map.append(sys.stdin.readline().split())
    #구름
    clouds.append([N-1, 0])
    clouds.append([N-1, 1])
    clouds.append([N-2, 0])
    clouds.append([N-2, 1])

def move(di, si):
    
    while clouds:
        cloud = clouds.popleft()
        col = cloud[0]
        row = cloud[1]
        n_col = (N + col + dx[di]*si) %N
        n_row = (N + row + dy[di]*si) %N
        





