# def solution(number, k):
#     answer = ''
#     stk = []
#     for i in number:
#         while stk and stk[-1] < i and k>0:
#             k-=1
#             stk.pop()
#         stk.append(i)
#     return "".join(stk[:len(stk)-k])



def solution(number, k):
    answer = ''
    maxNum = '-'
    nextNumIdx = 0
    index = 0
    # 초기 endPoint 설정
    totalLen=len(number)-k # 반환해야할 자리수 계산
    endPoint = -totalLen+1
    if endPoint == 0:
        prev = number[:]
    else:
        prev = number[:endPoint]
    # answer의 길이가 k가 될때까지 반복
    while True:
        if len(answer) == totalLen:
            break
        
        for i in range(len(prev)):
            # 더 큰 수를 만나면 maxNum 교체ㄴ
            if prev[i] > maxNum:
                maxNum = prev[i]
                index = i # 현재 인덱스 저장
                if maxNum == '9':
                    break

        answer += maxNum
        maxNum = '-' # maxNumber 초기화
        nextNumIdx += index + 1

        endPoint += 1
        if endPoint == 0:
            prev = number[nextNumIdx:]
        else:
            prev = number[nextNumIdx:endPoint]

    return answer