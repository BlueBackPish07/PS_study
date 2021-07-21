n = str(input())
n='abcd'    
answer = ""
for i in range(len(n)):
    if n[:i] == n[i:][::-1]:
        answer = n[:i] + n[i+1:][::-1]
        print(len(n)+i)
        break
    




