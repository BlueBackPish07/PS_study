def cut_str(s):
    length =[]
    result = ""
    
    if len(s)==1:  #문자열 길이가 1이면 결과는 무조건 1 
         return 1
    for cut in range(1, len(s)//2+1): #1 부터 문자열의 절반까지 자르며 비교해야하기떄문에
        temp = s[:cut]     #초기값 설정
        num = 1
        for i in range(cut, len(s), cut): #정해진 길이를 문자열 s의 길이까지 정해진 길이 스텝으로 반복
            if s[i:i+cut] == temp:    #만약 다음으로 자른값과 같을경우
                num+=1      #숫자 올려줌 (문자열 앞에 붙을 숫자)
            else:       #다를 경우
                if num == 1:  #숫자가 1 이면 문자열에 붙지 않으므로 없애줌
                    num=""
                result += str(num)+temp   #결과값에 숫자와 temp에 저장된 값을 저장
                temp = s[i:i+cut]   #temp값을 변경
                num=1       #숫자 다시 초기화
        if num == 1:  #else로 끝날을때만 저장이 되므로 반복
            num=""
        result +=str(num)+temp
        length.append(len(temp))
        temp=""
    return min(length) #최소값을 반환