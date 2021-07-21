

# n = int(input())
# arr= []
# for i in range(n):
#     temp = arr.append(input())

# for i in range (len(arr)):
#     temp = arr[i]      
#     for j in range(len(arr[i])-1):
#         if (temp[j] == temp[j+1]):
#             while (len(temp)>=1) :
#                 if temp[j] == "a":
#                     temp = re.sub("aa+", "", temp, 1)
#                 if temp[j] == "b":
#                     temp= re.sub("bb+", "",temp, 1)
#             if (len(temp) == 1):
#                 arr[i] = 1
#             if(len(temp) == 0):
#                 arr[i]=0
#             break
    
#아닌데.. 다섯시간동안 뻘짓하기


import re

def solve(s):
    group = [(m.start(0), m.end(0)) for m in re.finditer('aa+|bb+', s)]
    if len(group) == 0: return 0
    if len(set(s)) == 1: return 1
    for g in group:
        if solve(s[0:g[0]] + s[g[1]:]) == 1: return 1
    return 0

strings = [input() for _ in range(int(input()))]
for string in strings:
    print(solve(string))
