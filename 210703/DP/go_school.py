
def solution(m, n, puddles):
    mapp = [[0] * (m+1) for _ in range(n+1)]  #왼쪽벽과 위쪽벽을 0으로 채우기 위해 한칸을 늘려서 맵을 만들었다.
    mapp[1][1] = 1 #0,0이 아니고 1,1로 주어진다.
    for x in range(1, n+1):
        for y in range(1, m+1):
            if x == 1 and y == 1: # 시작점일 경우 무시
                continue
                
            if [y, x] in puddles: # 물웅덩일 경우 지나가지 못함으로 0 
                mapp[x][y] = 0  #문제에서 [a,b]로 주어지면 실제 배열에는 [b,a]로 나타나기 때문에 주의
            else:
                mapp[x][y] = mapp[x-1][y] + mapp[x][y-1] # 맵에 왼쪽으로 진입하는 경우의 수와 오른쪽으로 진입하는 경우의 수를 저장한다.
                                                    
    return mapp[-1][-1] % 1000000007 #오른쪽 하단의 값이 답이다.

