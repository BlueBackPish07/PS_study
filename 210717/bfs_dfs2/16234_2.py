from collections import deque
#https://dailyheumsi.tistory.com/61
dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

def bfs(x, y):
    visited = set([(x, y)])
    q = deque([(x, y)])

    """
    total : 연합의 인구수
    num : 연합에서 나라의 갯수
    """
    total, num = 0, 0

    while q:
        x, y = q.popleft()

        # 방문한 현재 나라의 인구수를 연합의 인구수에 더해주고, 연합에 속한 나라도 증가해준다.
        total += board[x][y]
        num += 1

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if nx >= 0 and nx < n and ny >= 0 and ny < n and (nx, ny) not in visited\
                and (nx, ny) not in total_visited:

                diff = abs(board[nx][ny] - board[x][y])
                if diff >= l and diff <= r:
                    # BFS를 한 번이라도 탄 것이므로, is_move를 True로 변환.
                    global is_move
                    is_move = True

                    q.append((nx, ny))
                    visited.add((nx, ny))

    # 이 연합의 바뀔 인구수와, 연합에 속한 나라(좌표)들을 반환한다.
    return total // num, visited

n, l, r = list(map(int, input().split()))
board = [list(map(int, input().split())) for _ in range(n)]
answer = 0

while True:
    total_visited = set() # BFS 탐색에 한번이라도 들어간 경우, 재 탐색을 할 필요가 없으므로,
                          # 이 집합에 담아둔다.
    is_move = False       # 한 번이라도 BFS를 타게되면 True로 바뀐다.
    unions = []           # (바뀔 인구수, 연합의 좌표들)을 담는다.

    # 먼저, 연합들을 찾아서 unions에 담는다.
    for i in range(n):
        for j in range(n):
            if (i, j) not in total_visited:
                changed_num, visited = bfs(i, j)
                unions.append((changed_num, visited))
                total_visited |= visited

    # 찾은 연합들의 좌표들을 일괄적으로 바꿔준다.
    for (changed_num, union) in unions:
        for country in union:
            x, y = country
            board[x][y] = changed_num

    # 한 번이라도 BFS를 타고들어갔는지 확인한다.
    if not is_move:
        break
    answer += 1

print(answer)