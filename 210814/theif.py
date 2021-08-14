def solution(money):
    dp = list([0] * len(money))
    
    #첫집을 훔칠경우
    dp[0] = money[0]
    dp[1] = dp[0]
    for i in range(2, len(money)-1):
        dp[i] = max(dp[i-1], dp[i-2] + money[i])
    maxVal = max(dp)
    
    #두번째 집부터 훔칠 경우
    dp = list([0] * len(money))
    dp[1] = money[1]
    for i in range(2, len(money)):
        dp[i] = max(dp[i-1], dp[i-2] + money[i])

    return max(max(dp), maxVal)