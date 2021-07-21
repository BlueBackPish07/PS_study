import sys
input = sys.stdin.readline
N = int(input())
arr= []
for i in range(N):
    arr.append(int(input()))
dp = []
dp.append(arr[0]) 
dp.append(max(arr[0] + arr[1], arr[1] ))
dp.append(max(arr[0] + arr[2] , arr[1] +arr[2]))
for i in range(3, N):
    dp.append(max(arr[i] + dp[i-2], arr[i] + arr[i-1] + dp[i-3]))

print(dp[-1])



# 성공코드 

# import sys
# input = sys.stdin.readline

# N = int(input())
# dp = [0 for _ in range(N+3)]
# arr = [0 for _ in range(N+3)]
# for k in range(1,N+1):
#     arr[k] = int(input())


# dp [1] = arr[1]
# dp [2] = arr[1] + arr[2]
# dp [3] = max(arr[1] + arr[3] ,arr[2] + arr[3])


# for i in range(4, N+1):
#     dp[i] = max(dp[i-3] + arr[i-1] + arr[i] ,  dp[i-2] + arr[i] ) 
# print(dp[N])