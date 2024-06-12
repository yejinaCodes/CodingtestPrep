import sys
input = sys.stdin.readline

def move(i, j, dr):
    back = -1
    for cnt in range(1, 10): # 최대로 뻡어서 벽을 만날때까지
        ni, nj = i + di[dr]*cnt, j + dj[dr]*cnt
        if arr[ni][nj] == '#':
            return cnt + back
        if arr[ni][nj] == 'O':
            return cnt
        # 다른 공을 지나간 경우 벽을 만났다면 한칸 뒤로
        if arr[ni][nj] == 'B' or arr[ni][nj] == 'R':
            back -= 1 # return 은 위에서만 처리해준다.



def dfs(n, ri, rj, bi, bj):
    global ans

    if (n, ri, rj, bi, bj) in v_set: # 이미 이 시도회수에 이 좌표조합을 해 봤음
        return
    v_set.add((n, ri, rj, bi, bj)) # 이후 중복체크 방지를 위해서 방문표시

    if n >= ans:
        return
    
    if n > 10: # 종료조건: 10회 이하까지만 진행
        return
    
    
    for dr in range(4): # 4방향으로 구슬 이동
        # 1. 각 공의 이동거리 계산
        r_cnt = move(ri, rj, dr) # 해당 방향으로 이동거리
        b_cnt = move(bi, bj, dr)
        if r_cnt == 0 and b_cnt == 0: # 이 방향으로는 탐색 불가
            continue
            
        # 2. 각 공의 이동 반영
        nri, nrj = ri + di[dr]*r_cnt, rj + dj[dr]*r_cnt
        nbi, nbj = bi + di[dr]*b_cnt , bj + dj[dr]*b_cnt

        # 3. 이동한 위치가 홀인 경우 처리(성공/실패)
        if arr[nbi][nbj] == 'O': # 파란색 공 -> 홀: 실패
            continue
        else:
            if arr[nri][nrj] == 'O': # 빨간색 공 -> 홀: 성공
                ans = min(ans, n)
                return
        # 4. 둘다 홀이 아닌경우 (next 좌표 기준으로 다음 시도)
        # 현재위치를 빈칸, 이동할 위치에 'R', 'B' 구슬표시
        arr[ri][rj], arr[bi][bj] = '.', '.'
        arr[nri][nrj], arr[nbi][nbj] = 'R', 'B'

        dfs(n+1, nri, nrj, nbi, nbj)

        arr[nri][nrj], arr[nbi][nbj] = '.', '.' # 반드시 원상 복구
        arr[ri][rj], arr[bi][bj] = 'R', 'B'




di = [-1, 1, 0, 0] # 상하좌우
dj = [0, 0,-1, 1]

#지도 입력 및 빨간색(ri,rj), 파란색(bi,bj) 초기좌표
N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'R':
            ri, rj = i, j
        if arr[i][j] == 'B':
            bi, bj = i, j

v_set = set() # 해당 시도회수때 R,B 구슬좌표가 같다면 -> 이미 해본 경우
# max값으로 지정
ans = 11
dfs(1, ri, rj, bi, bj)
if ans == 11:
    ans = -1
print(ans)