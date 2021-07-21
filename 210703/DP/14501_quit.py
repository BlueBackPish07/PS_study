# https://jrc-park.tistory.com/m/119 <움짤로 해석잘됨

#입력
n = int(input())
T = [0 for i in range(n+1)] #마지막날을 핸들링하기 위해서 한칸 더 만듦.
P = [0 for i in range(n+1)]

for i in range(n):  
    a, b = map(int, input().split())
    T[i] = a
    P[i] = b

# 풀이
dp= [0 for i in range(n+1)]

for i in range(n-1, -1, -1): # n번째 날의 정보는 n-1 에 들어있음으로 n-1부터 시작하고, 첫째날의 정보는 0에 있으므로 -1까지 진행한다
    if T[i]+i <=n: #날짜를 초과하지 않으면
        dp[i] =max (P[i]+ dp[i + T[i]], dp[i+1]) # 그날을 선택함과, 선택하지 않고 지나갈때와 비교한다.
    else:# 날짜를 초과하면
        dp[i] = dp[i+1] # 값을 복사해 준다.

print(dp[0])

    
