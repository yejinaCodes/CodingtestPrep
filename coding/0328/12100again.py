import sys
from copy import deepcopy
input = sys.stdin.readline

#input
N = int(input())
board = []
for i in range(N):
    board.append(list(map(int,input().split())))

result = 0

def max_board(board):
    maximum = 0
    for i in range(len(board)):
        maximum = max(maximum, max(board[i]))
    return maximum

def move(board, direction):
    inprocess = [[0]*N for _ in range(N)]
    #print(inprocess)

    if direction == 'top' or 'down': #상  하
        #column
        #c = []
        for j in range(N):
            t = []
            for i in range(N):
                if board[i][j] != 0:
                    t.append(board[i][j])

            if direction == 'top':
                for x in range(len(t)):
                    inprocess[x][j] = t[x]
            elif direction == 'down':
                t = t[::-1]
                for x in range(len(t)):
                    inprocess[N-1-x][j] = t[x]

        return inprocess

    #print('check', inprocess)
    elif direction == 'left' or 'right': #좌 우
        #print('h')
        for i in range(N):
            t = []
            for j in range(N):
                if board[i][j] != 0:
                    t.append(board[i][j])

            if direction == 'left':
                for x in range(len(t)):
                    inprocess[i][j] = t[x]
            elif direction == 'right':
                t = t[::-1]
                for x in range(len(t)):
                    inprocess[i][N-1-x] = t[x]
                    print(x, t[x])

        #print('check', inprocess)
        return inprocess

def collide(board, direction):
    dx = [-1, 1, 0, 0]  # 상하좌우
    dy = [0, 0, -1, 1]

    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                continue
            x, y = i,j
            if direction == 'top':
                nx = dx[0] + x
                ny = dy[0] + y
                if nx>= 0 and nx < N and ny>=0 and ny < N and board[x][y] == board[nx][ny]:
                    board[nx][ny] += board[x][y]
            elif direction == 'down':
                nx = dx[1] + x
                ny = dy[1] + y
                if nx>= 0 and nx < N and ny>=0 and ny < N and board[x][y] == board[nx][ny]:
                    board[nx][ny] += board[x][y]
            elif direction == 'left':
                nx = dx[2] + x
                ny = dy[2] + y
                if nx>= 0 and nx < N and ny>=0 and ny < N and board[x][y] == board[nx][ny]:
                    board[nx][ny] += board[x][y]
            elif direction == 'right':
                nx = dx[3] + x
                ny = dy[3] + y
                if nx>= 0 and nx < N and ny>=0 and ny < N and board[x][y] == board[nx][ny]:
                    board[nx][ny] += board[x][y]

    return board

direction = ['top', 'down', 'left', 'right']

def backtracking(board, count):
    if count == 5:
        maximum = max_board(board)
        result = max(result, maximum)
        return

    for d in range(4):
        tmp = deepcopy(board)
        tmp = move(tmp, direction[d])
        tmp = collide(tmp, direction[d])
        tmp = move(tmp, direction[d])
        backtracking(tmp, count+1)

backtracking(board, 0)
print(result)
print(max(result))