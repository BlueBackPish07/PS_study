import string
number = [0,1,2,3,4,5,6,7,8,9]
alpa = [i for i in string.ascii_lowercase]

cnt =0
case = input()
def sol(i, chr):
    global cnt
    if len(case) == i :
        cnt +=1
        return 
    if case[i] == 'd' : #숫자
        for j in number:
            if j != chr:
                sol(i+1, j)
    if case[i] == 'c': 
        for j in alpa:
            if j != chr:
                sol(i+1, j)

      
    
   

sol(0,' ')

print(cnt)

