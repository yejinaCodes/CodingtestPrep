import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
board = []
for i in range(N):
    tmp = list(input())
    del(tmp[-1])
    board.append(tmp)

red = []
blue = []
hole = []

cnt = 1e9

for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            red.append([i,j])
        elif board[i][j] == 'B':
            blue.append([i,j])
        elif board[i][j] == 'O':
            hole.append([i,j])

# bfs 안에 dfs 구현해야 함?

dx = [-1, 0, 1, 0] # 상 우 하 좌
dy = [0, 1, 0, -1]

visited_red = [[False] * M for _ in range(N)]
visited_blue = [[False] * M for _ in range(N)]

def move(x, y, color, direction):
    global visited_red, visited_blue, board, blue, red
    if color == 'R':
        while True:
            #print(direction)
            nx = dx[direction] + x
            ny = dy[direction] + y
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                break
            if board[nx][ny] == '#' or board[nx][ny] == 'B' or visited_red[nx][ny] == True:
                break
            if board[nx][ny] == '.':
                board[nx][ny] = 'R'
                board[x][y] = '.'
                visited_red[nx][ny] = True
                #red[0][0], red[0][1] = nx, ny
                x = nx
                y = ny
            elif board[nx][ny] == 'O':
                board[x][y] = '.'
                #print(board[x][y])
                return True

        return False

    elif color == 'B':
        while True:
            nx = dx[direction] + x
            ny = dy[direction] + y
            #print(board[nx][ny])
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                break
            if board[nx][ny] == '#' or board[nx][ny] == 'R' or visited_blue[nx][ny] == True:
                break
            if board[nx][ny] == '.':
                x = nx
                y = ny
                visited_blue[nx][ny] = True
                board[nx][ny] = 'B'
                blue[0][0], blue[0][1] = nx, ny
                board[nx][ny] = '.'
            elif board[nx][ny] == 'O':
                board[x][y] = '.'
                return True
            
        return False


redx, redy = red[0][0], red[0][1]
q = deque()
q.append((redx, redy, 0))

while q:
    x, y, count = q.popleft()

    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if board[nx][ny] == '#' or board[nx][ny] == 'B':
            #print(board[nx][ny], nx, ny)
            continue
        else:
            # R 움직이기
            check_red = move(x, y, 'R', i)
            #print(check_red)
            # O으로 탈출하지는 않았지만 R구술이 움직였다면 count += 1
            if not check_red:
                count += 1
                q.append((red[0][0], red[0][1], count))
            # O으로 탈출했을 경우
            elif check_red:
                count += 1
                cnt = min(cnt, count)

            # B 움직이기 
            check_blue = move(blue[0][0], blue[0][1], 'B', i )
            #print(check_blue)
            if not check_blue:
                continue
            elif check_blue:
                # print(cnt)
                print(-1)
                sys.exit()

print(cnt)