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
        temp_arr = list(dp_arr[i-1])#set요소는 정렬되지않으므로 리스트에 복사
        for k in temp_arr:
            dp_arr[i].add(k - N)
            dp_arr[i].add(N - k) #!
            dp_arr[i].add(k + N)
            dp_arr[i].add(k * N)
            
            if (N != 0):
                dp_arr[i].add(k // N)
            if (k != 0):
                dp_arr[i].add(N // k)
            
            if number in dp_arr[i]:
                return i+1

    
    return -1

print(solution(5,12))
