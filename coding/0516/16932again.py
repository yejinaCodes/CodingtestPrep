import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
map_ = []
for _ in range(N):
    map_.append(list(map(int, input().split())))

zeros = []
for i in range(N):
    for j in range(M):
        if map_[i][j] == 0:
            zeros.append((i,j))

groups = {}
visited = [[False]* M for _ in range(N)]
dx = [-1, 1, 0, 0] #상하좌우
dy = [0, 0, -1, 1]

def bfs(x, y, group):
    global groups, visited
    q = deque()
    q.append((x,y))
    while q:
        i, j = q.popleft()
        visited[i][j] = True
        map_[i][j] = group
        if group in groups.keys():
            groups[group] += 1
        else:
            groups[group] = 1

        for _ in range(4):
            nx = dx[_] + i
            ny = dy[_] + j
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if visited[nx][ny] == True:
                continue
            if map_[nx][ny] == 1:
                q.append((nx, ny))
                visited[nx][ny] = True

#grouping하기
group = 1
for i in range(N):
    for j in range(M):
        if map_[i][j] == 1 and visited[i][j] == False:
            bfs(i,j, group)
            group += 1

result = -1
for i in range(len(zeros)):
    x, y = zeros[i][0], zeros[i][1]
    tmp = set()
    for _ in range(4):
        nx = dx[_] + x
        ny = dy[_] + y
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if map_[nx][ny] != 0:
            tmp.add(map_[nx][ny])
    if len(tmp) == 0:
        continue
    else:
        tmp = list(tmp)
        total = 1
        for _ in range(len(tmp)):
            total += groups[tmp[_]]
        result = max(result, total)

print(result)