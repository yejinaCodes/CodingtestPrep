import sys
from collections import deque
input = sys.stdin.readline

def move(rr, rc, br, bc, d):
    dist_r = dist_b = 0
    # red
    while True:
        nrr, nrc = rr+dr[d], rc+dc[d]
        if board[nrr][nrc] == '#':
            break
        if board[nrr][nrc] == 'O':
            rr, rc = nrr, nrc
            break
        rr, rc = nrr, nrc
        dist_r += 1
    
    # blue
    while True:
        nbr, nbc = br+dr[d], bc+dc[d]
        if board[nbr][nbc] == '#':
            break
        if board[nbr][nbc] == 'O':
            br, bc = nbr, nbc
            break
        br, bc = nbr, nbc
        dist_b += 1
    return (rr, rc, br, bc, dist_r, dist_b)

    # check = -1
    # for i in range(1, 10):
    #     ni, nj = dx[d]+i, dy[d]+j
    #     if board[ni][nj] == '#':
    #         return (i + check)
    #     if board[ni][nj] == 'O':
    #         return i
    #     if board[ni][nj] == 'R' or board[ni][nj] == 'B':
    #         check -= 1

def bfs():
    while Q:
        rr, rc, br, bc, depth = Q.popleft()
        for i in range(4):
            nrr, nrc, nbr, nbc, dist_r, dist_b = move(rr, rc, br, bc, i)

            # 구멍에 둘다 빠지는 경우
            if board[nrr][nrc] == 'O' and board[nbr][nbc] == 'O':
                continue
            # 파란색 공이 구멍에 빠지는 경우
            if board[nbr][nbc] == 'O':
                continue
            # 빨간색 공만 구멍에 빠지는 경우
            if board[nrr][nrc] == 'O':
                return depth + 1
            
            # 동일 위치 처리. 구멍에 빠지 않았을 경우, 두 공다 동일한 위치에 있을 수 있기 때문
            if nrr == nbr and nrc == nbc:
                # 빨간공이 더 움직였을 경우
                if dist_r > dist_b:
                    nrr -= dr[i]
                    nrc -= dc[i]
                else:
                    # 파란공이 더 움직였을 경우
                    nbr -= dr[i]
                    nbc -= dc[i]
            # 해당 방향으로 움직인 경우가 존재하지 않을 경우에만 Q에 추가
            if not visited[nrr][nrc][nbr][nbc]:
                visited[nrr][nrc][nbr][nbc] = True
                Q.append([nrr, nrc, nbr, nbc, depth+1])
    
    return -1
    # global answer

    # # 빨간공과 파란공 옮기는 순서를 신경쓰기보다 generalize할 수 있는지를 생각해야 함
    # # 즉, 두 공 모두 동시에 움직인다고 생각해야 함.
    # for d in range(4):
    #     # 4방향마다 move함수 호출
    #     nri, nrj = move(ri, rj, d)
    #     nbi, nbj = move(bi, bj, d)

    #     # 두 공다 벽으로 인해 못 옮겼을 경우 
    #     if (nri, nrj, nbi, nbj) == (ri, rj, bi, bj):
    #         continue

N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            rr, rc = i, j
        if board[i][j] == 'B':
            br, bc = i, j

dr = [-1, 0, 1, 0] # 상우하좌
dc = [0, 1, 0, -1]
Q = deque([(rr, rc, br, bc, 0)])
# 4차원을 사용해야 하는 이유: 2공이 '동시'에 굴러가야 하기 때문. 
# 순서가 존재하면 예외케이스가 너무 많음. 하나의 구술의 visited 경로가
# 다른 구슬의 움직임을 제한하면 안되기 때문...
visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
visited[rr][rc][br][bc] = True
print(bfs())
