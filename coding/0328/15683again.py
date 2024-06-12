import sys
from copy import deepcopy
input = sys.stdin.readline

N,M = map(int,input().split())
room = []
for i in range(N):
    room.append(list(map(int,input().split())))

cctvs = []
for i in range(N):
    for j in range(M):
        if room[i][j] != 0 and room[i][j] != 6:
            cctvs.append((i,j))
result = 1e9

def calculatearea(n):
    global result
    total = 0
    for i in range(N):
        for j in range(M):
            if n[i][j] == 0:
                total += 1
    if total < result:
        result = total
    return

def cameraone(tmp,x,y,i):
    if i == 0:
        #하나의 column만 보기
        for r in range(x-1, -1, -1):
            if tmp[r][y] == 6:
                break
            if tmp[r][y] == 0:
                tmp[r][y] = -1
            else:
                continue
    elif i == 1:
        for c in range(y+1, M):
            if tmp[x][c] == 6:
                break
            if tmp[x][c] == 0:
                tmp[x][c] = -1
    elif i == 2:
        for r in range(x+1, N):
            if tmp[r][y] == 6:
                break
            if tmp[r][y] == 0:
                tmp[r][y] = -1
            else:
                continue
    elif i == 3:
        for c in range(y-1, -1, -1):
            if tmp[x][c] == 6:
                break
            if tmp[x][c] == 0:
                tmp[x][c] = -1
    return

def cameratwo(tmp,x,y,i):
    if i == 0:
        for c in range(y-1,-1,-1):
            if tmp[x][c] == 6:
                break
            if tmp[x][c] == 0:
                tmp[x][c] = -1
        for c in range(y+1, M):
            if tmp[x][c] == 6:
                break
            if tmp[x][c] == 0:
                tmp[x][c] = -1
    elif i == 1:
        for r in range(x-1,-1,-1):
            if tmp[r][y] == 6:
                break
            if tmp[r][y] == 0:
                tmp[r][y] = -1
        for r in range(x+1, N):
            if tmp[r][y] == 6:
                break
            if tmp[r][y] == 0:
                tmp[r][y] = -1
    return

def camerathree(tmp,x,y,i):
    if i == 0:
        for r in range(x-1, -1,-1):
            if tmp[r][y] == 6:
                break
            if tmp[r][y] == 0:
                tmp[r][y] = -1
        for c in range(y+1, M):
            if tmp[x][c] == 6:
                break
            if tmp[x][c] == 0:
                tmp[x][c] = -1
    elif i == 1:
        for c in range(y+1, M):
            if tmp[x][c] == 6:
                break
            if tmp[x][c] == 0:
                tmp[x][c] = -1
        for r in range(x+1, N):
            if tmp[r][y] == 6:
                break
            if tmp[r][y] == 0:
                tmp[r][y] = -1
    elif i == 2:
        for r in range(x+1, N):
            if tmp[r][y] == 6:
                break
            if tmp[r][y] == 0:
                tmp[r][y] = -1
        for c in range(y-1,-1,-1):
            if tmp[x][c] == 6:
                break
            if tmp[x][c] == 0:
                tmp[x][c] = -1
    elif i == 3:
        for c in range(y-1,-1,-1):
            if tmp[x][c] == 6:
                break
            if tmp[x][c] == 0:
                tmp[x][c] = -1
        for r in range(x-1, -1,-1):
            if tmp[r][y] == 6:
                break
            if tmp[r][y] == 0:
                tmp[r][y] = -1

    return

def camerafour(tmp,x,y,i):
    if i == 0:
        for r in range(x - 1, -1, -1):
            if tmp[r][y] == 6:
                break
            if tmp[r][y] == 0:
                tmp[r][y] = -1
        for c in range(y-1,-1,-1):
            if tmp[x][c] == 6:
                break
            if tmp[x][c] == 0:
                tmp[x][c] = -1
        for c in range(y+1, M):
            if tmp[x][c] == 6:
                break
            if tmp[x][c] == 0:
                tmp[x][c] = -1

    elif i == 1:
        for c in range(y + 1, M):
            if tmp[x][c] == 6:
                break
            if tmp[x][c] == 0:
                tmp[x][c] = -1
        for r in range(x-1,-1,-1):
            if tmp[r][y] == 6:
                break
            if tmp[r][y] == 0:
                tmp[r][y] = -1
        for r in range(x+1, N):
            if tmp[r][y] == 6:
                break
            if tmp[r][y] == 0:
                tmp[r][y] = -1

    elif i == 2:
        for r in range(x + 1, N):
            if tmp[r][y] == 6:
                break
            if tmp[r][y] == 0:
                tmp[r][y] = -1
        for c in range(y-1,-1,-1):
            if tmp[x][c] == 6:
                break
            if tmp[x][c] == 0:
                tmp[x][c] = -1
        for c in range(y+1, M):
            if tmp[x][c] == 6:
                break
            if tmp[x][c] == 0:
                tmp[x][c] = -1

    elif i == 3:
        for c in range(y - 1, -1, -1):
            if tmp[x][c] == 6:
                break
            if tmp[x][c] == 0:
                tmp[x][c] = -1

        for r in range(x-1,-1,-1):
            if tmp[r][y] == 6:
                break
            if tmp[r][y] == 0:
                tmp[r][y] = -1
        for r in range(x+1, N):
            if tmp[r][y] == 6:
                break
            if tmp[r][y] == 0:
                tmp[r][y] = -1
    return

def camerafive(tmp,x,y):
    for r in range(x+1, N):
        if tmp[r][y] == 6:
            break
        if tmp[r][y] == 0 :
            tmp[r][y] = -1
    for r in range(x-1,-1,-1):
        if tmp[r][y] == 6:
            break
        if tmp[r][y] == 0 :
            tmp[r][y] = -1
    for c in range(y+1, M):
        if tmp[x][c] == 6:
            break
        if tmp[x][c] == 0 :
            tmp[x][c] = -1
    for c in range(y-1,-1,-1):
        if tmp[x][c] == 6:
            break
        if tmp[x][c] == 0 :
            tmp[x][c] = -1



def backtracking(board, cameras):
    if len(cameras) == 0:
        calculatearea(board)
        return

    x, y = cameras.pop()
    if board[x][y] == 1:
        for i in range(4):
            tmp = deepcopy(board)
            cameraone(tmp,x,y,i)
            backtracking(tmp, cameras)
    elif board[x][y] == 2:
        for i in range(2):
            tmp = deepcopy(board)
            cameratwo(tmp,x,y,i)
            backtracking(tmp, cameras)
    elif board[x][y] == 3:
        for i in range(4):
            tmp = deepcopy(board)
            camerathree(tmp,x,y,i)
            backtracking(tmp, cameras)
    elif board[x][y] == 4:
        for i in range(4):
            tmp = deepcopy(board)
            camerafour(tmp,x,y,i)
            backtracking(tmp, cameras)
    elif board[x][y] == 5:
        tmp = deepcopy(board)
        camerafive(tmp,x,y)
        backtracking(tmp,cameras)


backtracking(room, cctvs)
print(result)