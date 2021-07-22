from collections import deque 
dxs = [-1, -1, 0, 1, 1, 1, 0, -1] 
dys = [0, 1, 1, 1, 0, -1, -1, -1] 
# n, m, k 입력 
n, m, k = list(map(int, input().split())) 



#뿌릴 양분을 담음 
nut = [list(map(int, input().split())) for _ in range(n)] 
#현재양분 
board = [[5]*n for _ in range(n)] 

trees_dict = {(i,j): deque() for i in range(n) for j in range(n)} 

for _ in range(m): 
  x, y, age = list(map(int, input().split())) 
  trees_dict[(x-1, y-1)].append(age) 
year = 0 
while True: 
  #죽은 나무들이 남길 양분
  added_nut = [[0]*n for _ in range(n)] 
  # 봄 
  for (x, y), trees in trees_dict.items(): 
    surived_trees = deque() # 나이가 어린 나무부터 
    for tree in trees: 
      if board[x][y] >= tree: 
        # 봄에는 나무가 자신의 나이만큼 양분을 먹고, 나이가 1 증가
          surived_trees.append(tree + 1) 
          board[x][y] -= tree 
      else: 
        
        added_nut[x][y] += tree // 2 
        # 살아남은 나무들로 갱신
        
    trees_dict[(x, y)] = surived_trees 
  # 여름 
  # # 여름에는 봄에 죽은 나무가 양분으로 변하게 된다. 
  for (x, y), trees in trees_dict.items(): 
    board[x][y] += added_nut[x][y] 
  # 가을 
  new_trees = {(i,j): 0 for i in range(n) for j in range(n)} 
  for (x, y), trees in trees_dict.items(): 
    for tree in trees: 

      if tree % 5 == 0: 
      # 인접한 8개의 칸에 나이가 1인 나무 
        for dx, dy in zip(dxs, dys): 
          nx, ny = x + dx, y + dy 
          if nx >= 0 and nx < n and ny >= 0 and ny < n: 
            new_trees[(nx, ny)] += 1 
  for (x, y), size in new_trees.items(): 
    for _ in range(size): 
      trees_dict[(x, y)].appendleft(1) 
  # 겨울 

  for i in range(n): 
    for j in range(n): 
      board[i][j] += nut[i][j] 
      
  year += 1 
  # K년 후 
  if year == k: 
    answer = 0 
    for (x, y), trees in trees_dict.items():
      answer += len(trees) 
    print(answer) 
    break
