# -*- coding: utf-8 -*-

t = int(input())
for _ in range(t):
    n, m , k= map(int, input().split())
    #2차원 배열 만들기
    array = [[0]*m for _ in range(n)]
     #배추 위치 입력받기
    for i in range(k):
        x, y = map(int, input().split())
        array[y][x] =  1

    def solution(x, y):
        #탐색하기
        if array [x][y] == 0: 
            array[x,y] == 1
            solution(x-1, y)
            solution(x+1, y)
            solution(x,y+1)
            solution(x,y-1)
            return true
        return false

    result = 0
    for i in range(m):
        for j in range(n):
            if solution(i,j)==true:
                result += 1

    print(result)
        


        
        

