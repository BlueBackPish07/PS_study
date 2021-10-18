#https://programmers.co.kr/learn/courses/30/lessons/83201

def solution(scores):
    chart = []
    for i in range(len(scores)):
        temp = []
        list(temp.append(scores[j][i]) for j in range(len(scores)))

        if temp.count(max(temp)) == 1 and temp[i] == max(temp):
            del temp[i]
        elif temp.count(min(temp)) == 1 and temp[i] == min(temp):
            del temp[i]
            
        average = sum(temp) / len(temp)
        chart.append(average)

    for i in range(len(chart)):
        if chart[i] >= 90:
            chart[i] = 'A'
            continue
        if chart[i] >= 80:
            chart[i] = 'B'
            continue
        if chart[i]>=70:
            chart[i] = 'C'
            continue
        if chart[i]>=50:
            chart[i] = 'D'
            continue
        else:
            chart[i] = 'F'

    answer = ''.join(chart)
    return answer


print(solution([[50,90],[50,87]]))
print(solution([[70,49,90],[68,50,38],[73,31,100]]))