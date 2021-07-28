def solution(N, number):
    #n은 9 이하의수
    #number은 1 이상 32,000 이하
    dp_arr = list(set() for i in range(9))
    
    if N == number:
        return 1

    for i in range(len(dp_arr)):
        temp = str(N)*(i+1)
        dp_arr[i].add(int(temp))
        
    for i in range(1,len(dp_arr)): #dp_arr[0]은 무시, N 한개로 만들수 있는건 N 밖에없다.
        for half in range(0, i//2 +1): # 
            for front in dp_arr[half]: # 
                for back in dp_arr[(i - half)-1]: # 
                    dp_arr[i].add(front- back)
                    dp_arr[i].add(back - front) 
                    dp_arr[i].add(front + back)
                    dp_arr[i].add(front * back )
                    if (front != 0):
                        dp_arr[i].add(back // front)
                    if (back != 0):
                        dp_arr[i].add(front// back)
                
        if number in dp_arr[i]:
            return i+1
    
    return -1


print(solution(3,18),3)
