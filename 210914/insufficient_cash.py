#https://programmers.co.kr/learn/courses/30/lessons/82612
def solution(price, money, count):
    temp = [0]*(count+1)
    for i in range(count+1):
        temp[i] = price * i

    total_price = sum(temp)
    
    result = money - total_price

    if result > 0 :
        return 0

    return abs(result)

print(solution(3,20,4))

