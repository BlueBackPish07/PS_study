#https://programmers.co.kr/learn/courses/30/lessons/43105
def solution(triangle):

    if len(triangle) == 1:
        return triangle[0][0]
    if len(triangle) == 2:
        return max(triangle[1][0], triangle[1][1]) + triangle[0][0]
        
    triangle[1][0]+=triangle[0][0]
    triangle[1][1]+=triangle[0][0]
    for line in range(2,len(triangle)): #삼각형의 줄 수 만큼
        for mid in range(1,len(triangle[line])-1):
            triangle[line][mid] += max(triangle[line-1][mid-1],triangle[line-1][mid])

        triangle[line][0] += triangle[line-1][0]
        triangle[line][line] += triangle[line-1][line-1]

      
    answer = max(triangle[len(triangle)-1])
    return answer


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))