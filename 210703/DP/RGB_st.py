import sys
n = int(input())
cost = 0
index_list = []
for i in range(n):
    arr = list(map(int,sys.stdin.readline().split()))
    if i == 0:
        pick = min(arr)
        inD = arr.index(pick)
        index_list.append(inD)
        cost = cost + pick
        continue
    
    pick = min(arr)
    inD = arr.index(pick)

    if index_list[i-1] == inD:
        pick = min(arr[inD-1], arr[inD-2])
        inD = arr.index(pick)
    index_list.append(inD)
    cost = cost + pick

print(cost)


'''
3
1 2 3
2 1 3
99 1 101

일때 위 코드대로 처리하면 3번째 줄에서 99를 선택하게되니까.. 다른방식을 생각

'''