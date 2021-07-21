

# result = 0
# for i in "JEROEN":
#     index = findIndex(i)
#     if index - 13 >=  0:
#         move = 26 - index
#         result += move    
#     else:
#         move = index
#         result += move
        
# print(result)
    
def solution(name):
    LUT = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,12,11,10,9,8,7,6,5,4,3,2,1]
    answer = 0
    
    for c in name: #알파벳 조작
        answer += LUT[ord(c) - ord('A')]
    
    #위치조작
    n = len(name)
    left_or_right = n-1 # 글자가 다 앞쪽에 있을경우 오른쪽으로만 이동하여 조이스틱은 오른쪽으로 n-1번 이동한다.
    for i in range(n): #글자 길이만큼 반복한다.
        _next = i + 1
        
        while _next < n and name[_next] == 'A': #오른쪽으로 이동하면서 만난 글자가 A면 _next에 1을 올려서 저장한다.
            _next += 1
            
        left_or_right = min(left_or_right, i + n - _next + min(i, n-_next))
        #오른쪽으로만 갈 경우 (left or right) 와 ???
    answer += left_or_right
    return answer

