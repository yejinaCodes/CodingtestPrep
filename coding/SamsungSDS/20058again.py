import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def rotate_and_melting(board, len_board, L):
    new_board = [[0] * len_board for _ in range(len_board)]

    r_size = 2 ** L
    for x in range(0, len_board, r_size): #격자 시작 좌표
        for y in range(0, len_board, r_size): #격자 시작 좌표
            for j in range(r_size):
                for i in range(r_size):
                    #print(board[x+j][y+i])
                    new_board[x + i][y + r_size - j - 1] = board[x + j][y + i]

    board = new_board
    melting_list =[]
    for x in range(len_board):
        for y in range(len_board):
            ice_count = 0
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]

                if nx < 0 or ny < 0 or nx >= len_board or ny >= len_board:
                    continue
                elif board[nx][ny] > 0:
                    ice_count += 1

            if ice_count < 3 and board[x][y] != 0:
                melting_list.append((x,y))

    for x, y in melting_list:
        board[x][y] -= 1

def check_ice_bfs(board, len_board):
    used = [[False] * len_board for _ in range(len_board)]
    ice_sum = 0
    max_area_count = 0
    for x in range(len_board):
        for y in range(len_board):
            area_count = 0
            if used[x][y] or board[x][y] == 0:
                continue

            q = deque()
            q.append((x, y))
            used[x][y] = True

            while q:
                sx, sy = q.popleft()
                ice_sum += board[sx][sy]
                area_count += 1

                for d in range(4):
                    nx = sx + dx[d]
                    ny = sy + dy[d]
                    if nx < 0 or ny < 0 or nx >= len_board or ny >= len_board or used[nx][ny]:
                        continue
                    if board[nx][ny] != 0:
                        used[nx][ny] = True
                        q.append((nx, ny))

            #최대 얼음덩어리 크기
            max_area_count = max(max_area_count, area_count)
    print(ice_sum)
    print(max_area_count)

def solve():
    N, Q = map(int, input().split())
    len_board = 2 ** N
    board = [list(map(int, input().split())) for _ in range(len_board)]
    L_list = list(map(int,input().split()))

    for L in L_list:
        board = rotate_and_melting(board, len_board, L)

    check_ice_bfs(board, len_board)

solve()
