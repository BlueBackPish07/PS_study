import sys 
import math
input = sys.stdin.readline

def maxInit(start, end, node): #구간별로 최댓값을 저장
    if start == end:
        maxTree[node] = array[start]
        return maxTree[node]
    mid = (start + end) //2
    maxTree[node] = max(maxInit(start, mid, node*2), maxInit(mid+1, end, node*2+1))
    return maxTree[node]

def minInit(start, end, node): #구간별로 최솟값을 저장
    if start == end:
        minTree[node] = array[start]
        return minTree[node]
    mid =(start + end) // 2
    minTree[node] = min(minInit(start, mid, node*2), minInit(mid+1, end, node*2+1))
    return minTree[node]

def minFind(start, end, left, right, node): #left~right 사이의 최솟값 찾기
    if left > end or right < start :
        return math.inf
    if left <= start and end <= right: #범위 안에 겹칠 경우
        return minTree[node]
    mid = (start+end) // 2
    return min(minFind(start,mid, left, right, node*2), minFind(mid+1, end , left, right, node*2+1))

def maxFind(start, end, left, right, node):#left~right 사이의 최솟값 찾기
    if left > end or right < start :
        return -1
    if left <= start and end <= right: # 범위 안에 겹칠 경우 
        return maxTree[node]
    mid = (start+end) // 2   
    return max(maxFind(start, mid, left, right, node*2), maxFind(mid+1, end, left, right, node*2+1))

N, M = map(int, input().split())
array = []
minTree = [0]*(4*N)
maxTree = [0]*(4*N)
for i in range(N):
    array.append(int(input().rstrip()))

maxInit(0, N-1 , 1)
minInit(0, N-1, 1)

for i in range(M):
    left, right = map(int, input().split())
    print(minFind(0, N-1, left-1, right-1, 1), maxFind(0,N-1, left-1,right-1, 1))