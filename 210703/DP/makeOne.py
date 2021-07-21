n = int(input())
df=[0,0,1]
for i in range(3,n+1):
    df.append(df[i-1]+1) # 일단 1 늘린걸로 채우고
    if n%2 == 0 : 
        df[i] = min(df[i//2]+1, df[i]) # 2로 나눠서 접근했을때랑 비교
    if n%3 == 0 :
        df[i] = min(df[i//3]+1, df[i]) # 3으로 나눠서 접근했을때랑 비교
   
print(df[n])     
        