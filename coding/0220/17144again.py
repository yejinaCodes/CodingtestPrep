#다른 사람 풀이)

import sys
input = sys.stdin.readline

R,C,T = map(int,input().split())
board = [list(map(int,input().split())) for i in range(R)]
robot_top = 0
robot_bottom = 0

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def spread():
    change = [[0]*C for _ in range(R)]
    for x in range(R):
        for y in range(C):
            if board[x][y] > 0:
                tmp = 0
                for i in range(4):
                    ax = x +dx[i]
                    ay = y +dy[i]
                    if ax>=0 and ax<R and ay<C and ay>=0:
                        if board[ax][ay] != -1:
                            change[ax][ay] += board[x][y]//5
                            tmp += board[x][y]//5
                board[x][y] -= tmp
    for x in range(R):
        for y in range(C):
            board[x][y] += change[x][y]

def rotation():
    def top_rotate():
        d = 1
        before = 0
        x, y = robot_top, 1
        while True:
            ax = x + dx[d]
            ay = y + dy[d]
            if ax == R or ay == C or ax == -1 or ay == -1:
                d = (d-1)%4
                continue
            if x == robot_top and y == 0:
                break
            board[x][y], before = before, board[x][y]
            x,y = ax, ay
    def bottom_rotate():
        d = 1
        before = 0
        x, y = robot_bottom, 1
        while True:
            ax = x+ dx[d]
            ay = y+ dy[d]
            if ax == R or ay == C or ax == -1 or ay == -1:
                d = (d+1)%4
                continue
            if x == robot_bottom and y == 0:
                break
            board[x][y], before = before, board[x][y]
            x,y = ax,ay
    
    top_rotate()
    bottom_rotate()


for i in range(R):
    if board[i][0] == -1:
        robot_top = i
        robot_bottom = i+1
        break

for i in range(T):
    spread()
    rotation()

answer = 2
for i in range(R):
    answer += sum(board[i])
print(answer)