import sys
n, s = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
cnt = 0
def dfs(i, arr, total):
    global cnt, n, s
    if total == s:
        cnt +=1
    
    for j in range(i+1, n):
        dfs(j, arr, total + arr[j])
    


for i in range(0, n):
    dfs(i, arr, arr[i])
