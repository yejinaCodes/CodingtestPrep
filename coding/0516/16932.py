import sys
input = sys.stdin.readline

N, M = map(int, input().split())

maze = [list(map(int, input().split())) for _ in range(N)]
zeros = []
zero = 0

result = 0
dx = [-1, 0, 1, 0] #상 우 하 좌
dy = [0, 1, 0, -1]

for i in range(N):
    for j in range(M):
        if maze[i][j] == 0:
            count = 0
            for _ in range(4):
                nx = dx[_] + i
                ny = dy[_] + j
                if nx < 0 or nx >= N or ny < 0 or ny >= M:
                    continue
                if maze[nx][ny] == 1:
                    count += 1
            if count > zero:
                zero = count
                zeros = [(i, j)]
            elif count == zero:
                zeros.append((i,j))

# for i in range(N):
#     for j in range(M):
#         if maze[i][j] == 0:
#             zeros.append((i,j))


check = [[False] * M for _ in range(N)]
def bfs(x, y):
    global result, check
    q = []
    count = 0
    visited = [[False] * M for _ in range(N)]
    q.append((x, y))
    #visited[x][y] = True
    #count += 1 
    checks = []
    while q:
        i, j = q.pop()
        #visited[i][j] = True
        if maze[i][j] == 1 and visited[i][j] == False:
            count += 1
            visited[i][j] = True
            checks.append((i,j))
        for d in range(4):
            nx = dx[d] + i
            ny = dy[d] + j
            if nx < 0 or nx >= N or ny < 0 or ny >= M or maze[nx][ny] == 0 or visited[nx][ny] == True:
                continue
            if maze[nx][ny] == 1:
                q.append((nx, ny))
                #count += 1
                #visited[nx][ny] = True
    #print('result:', result, 'count:', count)
    #print(maze)
    result = max(result, count)
    # for _ in range(len(checks)):
    #     check[checks[_][0]][checks[_][1]] = True
    

for _ in range(len(zeros)):
    #print(zeros)
    x, y = zeros[_][0], zeros[_][1]
    #print('zerox:', x, 'zeroy:', y)
    maze[x][y] = 1
    bfs(x, y)
    # for i in range(N):
    #     for j in range(M):
    #         if maze[i][j] == 1:
    #             bfs(i, j)
    maze[x][y] = 0

print(result)