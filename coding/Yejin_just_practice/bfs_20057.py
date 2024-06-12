import sys
from collections import deque
input = sys.stdin.readline

N, M, K = map(int, input().split())
area = [[0 for _ in range(M)] for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
box = []
result = []
for _ in range(K):
    dm, dn, tm, tn = map(int, input().split())
    box.append([N-dn-1, dm, N-tn, tm-1])
#coloring
for _ in range(K):
    x, y, xx, yy = box[_]
    for i in range(x, xx-1, -1):
        for j in range(y, yy+1):
            area[i][j] = 1
            visited[i][j] = True
#bfs
def bfs(i,j):
    global area, visited, result
    dx = [-1, 1, 0, 0] #상하좌우
    dy = [0, 0, -1, 1]
    size = 0
    q = deque()
    q.append((i,j))
    while q:
        x, y = q.popleft()
        visited[x][y] = True
        size += 1
        for _ in range(4):
            nx = dx[_] + x
            ny = dy[_] + y
            if 0 <= nx < N and 0 <= ny < M and area[nx][ny] == 0 and visited[nx][ny] == False:
                q.append((nx, ny))
                visited[nx][ny] = True
    return size

for i in range(N):
    for j in range(M):
        if area[i][j] == 0 and visited[i][j] == False:
            result.append(bfs(i,j))
        
print(len(result))
result.sort()
print(*result)