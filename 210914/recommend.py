#https://programmers.co.kr/learn/courses/30/lessons/84325

def solution(table, languages, preference):
    arr = []
    for i in table:
        li= i.split()
        arr.append(li)
    job_score = []
    for row in arr:
        score = 0
        temp = [] #직업군 선호점수
        for ele in languages:
            #index에서 값이 없을때 0
            prefer_score = len(row) - (row.index(ele) if ele in row else len(row))
            temp.append(prefer_score)
        if len(temp) != len(preference):
            return 
        for i in range(len(preference)):
            score = score + (preference[i]*temp[i])
        job_score.append(score)

    answer = ''
    #동점 발생시 알파벳순으로선택
    if job_score.count(max(job_score)) > 1:
        str_chk = [i for i , value in enumerate(job_score) if value == max(job_score)]
        temp = []
        for i in str_chk:
            temp.append(arr[i][0])
        temp.sort()
        return str(temp[0])
    answer = str(arr[job_score.index(max(job_score))][0])
    return answer



# table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]

# languages = ["PYTHON", "C++", "SQL"]
# preference = [7, 5, 5]
# print(solution(table,languages,preference))


table=["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
languages=["JAVA", "JAVASCRIPT"]
preference =[7, 5]
solution(table, languages, preference)