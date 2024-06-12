import sys
from collections import deque
input = sys.stdin.readline

N, Q = map(int, input().split())
n = 2 ** N
ice_map = []
for _ in range(n):
    ice_map.append(list(map(int, input().split())))

#여러 단계일 수 있음.
L_list = list(map(int, input().split()))

def rotate90(matrix, L):
    global n
    newboard = [[0] * n for _ in range(n)] #회전한 board 저장용
    block_len = 2 ** L

    for x in range(0, n, block_len):
        for y in range(0, n, block_len):
            for i in range(block_len):
                for j in range(block_len):
                    newboard[x + j][y - i + block_len - 1] = matrix[x + i][y + j]

    return newboard

def ice_melt_bfs(matrix):
    global biggest_block, n
    #ice melt + 가장 큰 덩어리 차지하는 칸의 개수 계산하기

    dx = [-1, 1, 0, 0] #상하좌우
    dy = [0, 0, -1, 1]

    visited = [[False] * n for _ in range(n)]
    will_melt = deque()
    for i in range(n):
        for j in range(n):
            count = 0
            x, y = i, j
            for d in range(4):
                nx = dx[d] + x
                ny = dy[d] + y

                if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[nx][ny]:
                    continue

                elif matrix[nx][ny] != 0:
                    count += 1
            if count < 3 and matrix[x][y] != 0:
                will_melt.append((x,y))

    for i, j in will_melt:
        matrix[i][j] -= 1

    return matrix

def check_ice_bfs(matrix):
    global n, biggest_block
    dx = [-1, 1, 0, 0] #상하좌우
    dy = [0, 0, -1, 1]

    ice_sum = 0
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            count = 0
            q = deque()
            depth_count = 0
            if matrix[i][j] == 0 or visited[i][j]:
                continue

            q.append((i, j))
            visited[i][j] = True

            while q:
                x, y = q.popleft()
                count += 1
                ice_sum += matrix[x][y]

                for d in range(4):
                    nx = dx[d] + x
                    ny = dy[d] + y

                    if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[nx][ny]:
                        continue

                    if matrix[nx][ny] != 0:
                        visited[nx][ny] = True
                        q.append((nx,ny))

            biggest_block = max(biggest_block, count)

    return ice_sum

biggest_block = 0

for L in L_list:
    # 격자 돌리기
    ice_map = rotate90(ice_map, L)
    #녹이
    ice_map = ice_melt_bfs(ice_map)

ice_sum = check_ice_bfs(ice_map)

print(ice_sum)
print(biggest_block)
