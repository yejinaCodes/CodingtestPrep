import sys
import heapq
#input = sys.stdin.readline

M, N = map(int, input().split())

maze = [list(map(int, input())) for _ in range(N)]
#print(maze)
# maze = []
# for _ in range(N):
#     maze.append(list(map(str, input())))
#     maze[_].remove('\n')
#     maze[_] = int(maze[_])
# print(maze)

distance = [[1e9] * M for _ in range(N)]

dx = [-1, 0, 1, 0] #상우하좌
dy = [0, 1, 0, -1]

def dijkstra():
    q = []
    heapq.heappush(q, (0, 0, 0))
    distance[0][0] = 0
    while q:
        cost, r, c = heapq.heappop(q)

        if cost > distance[r][c]:
            continue

        for i in range(4):
            nx = dx[i] + r
            ny = dy[i] + c

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            #print(nx, ny)
            #print(maze[nx][ny])
            if cost + maze[nx][ny] < distance[nx][ny]:
                distance[nx][ny] = cost + maze[nx][ny]
                heapq.heappush(q, (distance[nx][ny], nx, ny))

dijkstra()
print(distance[N-1][M-1])