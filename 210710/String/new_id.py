import re
def solution(new_id):
    first = new_id.lower()
    #re.sub('패턴', '바꿀문자열', '문자열', 바꿀횟수)
    second = re.sub('[^a-z0-9\-\_\.]' ,'', first)
    third = re.sub('\.\.+', '.' , second)
    fourth = re.sub('^\.|\.$', '' , third)
    if fourth == '': #5단계
        fourth = 'a'
    
    if len(fourth) >=16: #6-1
        fourth = fourth[:15]
    if fourth[-1] == '.': #6-2
        fourth = fourth[:-1]
    
    while len(fourth) <=2:
        fourth = fourth + fourth[-1]
    
    return fourth



def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st
