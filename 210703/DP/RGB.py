import sys
n = int(input())

lis = []
for _ in range(n):
    temp = list(map(int,sys.stdin.readline().split()))
    lis.append(temp)

total_cost = [[0]*3 for _ in range(n)]

total_cost[0][0] = lis[0][0] 
total_cost[0][1] = lis[0][1] 
total_cost[0][2] = lis[0][2]

print(lis)
print(total_cost)

for i in range(1, n):
    total_cost[i][0] = min(total_cost[i-1][1],total_cost[i-1][2])+ lis[i][0]
    total_cost[i][1] = min(total_cost[i-1][0],total_cost[i-1][2])+ lis[i][1]
    total_cost[i][2] = min(total_cost[i-1][1],total_cost[i-1][1])+ lis[i][2]
    min_cost = min(total_cost[n-1][0], total_cost[n-1][1])
    min_cost = min(min_cost, total_cost[n-1][2])

print(min_cost)
