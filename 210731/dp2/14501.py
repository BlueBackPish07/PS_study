
import sys

N = int(input())
ti= []
pi=[]
for i in range(N):
    T , P = map(int, sys.stdin.readline().split())
    ti.append(T)
    pi.append(P)
ti.append(0)
pi.append(0)
dp = [0 for i in range(N+1)]

for i in range(N-1, -1, -1):
    if (ti[i]+ i) <= N: #그 날을 선택할 수 있다면
        dp[i] = max(dp[i+1], dp[i+ ti[i]]+ pi[i]) #선택하지 않은 경우와 선택한 경우를 비교한다.
    else: #선택할 수 없다면
        dp[i] = dp[i+1] #복사해준다.

print(dp[0])

        
