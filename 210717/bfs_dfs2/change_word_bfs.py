def solution(begin, target, words):
    from collections import deque
    
    graph={i:0 for i in words} #딕셔너리를 이용해 과정을 같이 저장한다. 
    graph[begin]=0
    
    queue=deque()
    queue.append(begin)
    
    while queue:
        now=queue.popleft()
        if now==target:
            break
        for word in words:
            cnt=0
            for a,b in zip(now,word):
                if a==b:
                    cnt+=1
            if cnt==len(word)-1 and graph[word]==0:# 한글자 차이가 나고 , graph가 0인(방문x)
                graph[word]=graph[now]+1 #단계를 저장하고
                queue.append(word) # 큐에 넣는다.
    
    if target in words:
        return graph[target]
    else:
        return 0

# 그래프에 모든 단어의 깊이값을 저장하게 된다.