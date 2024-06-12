import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

cheese_list = deque()
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            cheese_list.append((i,j))

dx = [-1, 0, 1, 0] #상우하좌
dy = [0, 1, 0, -1]

def bfs(i,j, current):
    q = deque()
    q.append((i,j))
    while q:
        x, y = q.popleft()
        board[x][y] = 2
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if board[nx][ny] == current:
                q.append((nx, ny))

#외부공기 2로 미리 세팅
bfs(0,0,0)

time = 0
while cheese_list:
    tmp_c = deque() #외부공기와 접촉해 곧 사라질 c. 
    touch_inandout = set() #c와 접속하고 있는 내부공기
    #모든 치즈에 대해서 사라질 c 찾기
    for c in cheese_list:
        x, y = c
        touch_air = 0
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if board[nx][ny] == 2:
                touch_air += 1

        if touch_air >= 2:
            tmp_c.append((x, y))
            board[x][y] = 2

    #c를 board에서 지우기
    while tmp_c:
        x, y = tmp_c.popleft()
        board[x][y] = 2
        cheese_list.remove((x,y))
        # for i in range(4):
        #     nx = dx[i] + x
        #     ny = dy[i] + y
        #     if nx < 0 or nx >= N or ny < 0 or ny >= M:
        #         continue
        #     if board[nx][ny] == 0:
        #         touch_inandout.add((nx, ny))

    #외부와 닿는 내부공기 2로 바꿔주기
    # while touch_inandout:
    #     x, y = touch_inandout.pop()
    #     bfs(x,y,0)
    bfs(0,0,0)

    time += 1

print(time)
    