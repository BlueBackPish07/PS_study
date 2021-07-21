# -*- coding: utf-8 -*-


def solution (number, k) : 
    nList = list(number) #문자열을 리스트로 
    nListLen = len(nList)  
    resultLen = nListLen - k #만들어야 하는 글자 수
    result = []
    index = -1
    i=0
    while(nListLen-i>0):
        if (index == -1):
            index =0
        j = nListLen-resultLen
        a= nList[index:j]
        maxNum = max(a) #그 중 가장 큰 수를 리턴하고 
        index = nList.index(maxNum) #가장 큰 수의 인덱스를 리턴한다.
        result.append(maxNum)
        index = index + 1
        i=i+1
        j=j-1
    answer = "".join(result)
    return answer
print(solution("1231234",3))




