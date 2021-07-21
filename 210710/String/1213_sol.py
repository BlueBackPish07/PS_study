s = str(input())

if len(s)==1 or s==s[::-1]: #길이가 1개거나 이미 펠린드롬인 경우
    print(len(s))
else:
    for i in range(len(s),0,-1): #뒤에서부터 자른 문자열이 펠린드롬인지 확인한다.
                                #역순으로 가는 이유는 가장 긴 펠린드롬을 기억하기 위해 ex) baaaaa 면 p = aaaaa
        if s[i:len(s)]==s[i:len(s)][::-1]: #자른 문자열이 펠린드롬이면
            #temp = s[i:len(s)]
            p = s[i:len(s)][::-1] #기억
    print(2 * len(s) - len(p)) #길이는 주어진 문자열*2 에서 펠린드롬의 길이를 뺀다.

# 문자열이라 reversed 를 쓰려니까 자꾸 타입에러가 나서 [::-1]을 활용하는게 편함