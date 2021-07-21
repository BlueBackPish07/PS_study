n = int(input())
wine = [0]
dp = [0]

for i in range(n):
    wine.append(int(input()))

dp.append(wine[1]) #와인이 한잔이면 한잔을 마신다
#dp.append(wine[1]+ wine[2]) # 와인이 두잔이면 두잔을 마신다. < 1잔 주어지면 wine[2] 는 없다.
if n > 1 : 
    dp.append(wine[1]+wine[2])

for i in range(3, n+1) : #이후부터 와인을 선택하는 경우는 세가지이다.
    A = wine[i] +dp[i-2] #두칸전 와인을 마셨다고 가정하고, 현재 와인을 마신다.
    B = wine[i] + wine[i-1] +dp[i-3] # 현재와인과, 한칸전 와인을 마신다
    C = dp[i-1] #두잔 다 마시지 않고 지나간다.
    dp.append(max(A, B, C))

print(dp[n])
