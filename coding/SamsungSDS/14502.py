import sys
from copy import deepcopy
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
lab = []
for i in range(N):
    lab.append(list(map(int, input().split())))

virus = deque()
for i in range(N):
    for j in range(M):
        if lab[i][j] == 2:
            virus.append((i,j))

def bfs():
    global answer
    lab_copy = deepcopy(lab)

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    
    for i in range(N):
        for j in range(M):
            if lab_copy[i][j] == 2:
                #q = deque()
                #lab_copy[i][j] = -1
                queue.append((i,j))

    while queue:
        x, y = queue.popleft()
                    
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if lab_copy[nx][ny] == 0:
                queue.append((nx, ny))
                lab_copy[nx][ny] = 2

    cnt = 0
    for i in range(N):
        cnt += lab_copy[i].count(0)
    
    answer = max(answer, cnt)

# worstcase = bfs()
# print(worstcase)

def makeWall(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(N):
        for j in range(M):
            if lab[i][j] == 0:
                lab[i][j] = 1
                makeWall(cnt+1)
                lab[i][j] = 0

answer = 0
makeWall(0)
print(answer)