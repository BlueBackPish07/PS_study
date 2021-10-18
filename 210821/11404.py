import sys
import math
INF=sys.maxsize

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
arr= [[INF] * n+1 for _ in range(n+1)]


for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    arr[a][b] = c
    arr[b][a] = c

# 최소비용구하기
for k in range(n):
    for i in range(n):
        for j in range(n):
            arr[i+1][j+1] = min(arr[i+1][j+1], arr[i+1][k+1] + arr[k][j])

#출력 에서 시간이 많이 잡혀서 참고..
for i in range(n):
    for j in range(n):
        if arr[i+1][j+1] == INF:
            arr[i+1][j+1] = 0
        print(arr[i+1][j+1], end="")
    print()