from collections import deque
#import sys
#input = sys.stdin.readline
r, c, k = map(int, input().split())
checked_pos = []
heater = []

for i in range(r):
    tmp = list(map(int, input().split()))
    for j, t in enumerate(tmp):
        if t == 0:
            continue
        if 0 < t < 5:
            heater.append([i, j, t])
        else:
            checked_pos.append([i, j])

walls = [[[False]*5 for _ in range(c)] for _ in range(r)]
#허수, 우, 좌, 상, 하

for _ in range(int(input())):
    x, y, t = map(int, input().split())
    x -= 1
    y -= 1
    #horizontal
    if t == 0:
        #x,y의 상에 True
        walls[x][y][3] = True
        if x == 0:
            continue
        #x-1, y의 하에 True
        walls[x-1][y][4] = True #아래부분도 체크
    #vertical
    if t == 1:
        walls[x][y][1] = True
        if y == c-1:
            continue
        walls[x][y+1][2] = True

maps = [[0]*c for _ in range(r)]

#우좌상하
dxys =[[], [[-1,1], [0,1], [1,1]], [[-1,-1],[0,-1],[1,-1]], [[-1,1], [-1,0], [-1,1]], [[1,-1], [1,0], [1,1]]]

#matrix범위 안에 들어가 있는지 체크
def iscriteria(x,y):
    if 0 <= x < r and 0 <= y < c:
        return True
    return False

def isnext(x,y,t,idx):
    #직선방향일 경우
    if idx == 1:
        if walls[x][y][t]:
            return False
        else:
            return True
    if t == 1: #오른쪽
        nx = x + dxys[t][idx][0]
        if 0<= nx < r:
            t_walls = walls[nx][y]
            #대각선 상
            if idx == 0:
                #이 부분이 잘 이해가 안감..먼저 x,y의 대각선
                if t_walls[4] or t_walls[1]: #아래, 오른쪽
                    return False
                return True
            # 대각선 하
            else:
                if t_walls[3] or t_walls[1]:
                    return False
                return True
    if t == 2:
        nx = x + dxys[t][idx][0]
        if 0 <= nx < r:
            t_walls = walls[nx][y]
            if idx == 0:
                if t_walls[4] or t_walls[2]: #아래, 왼쪽
                    return False
                return True
            else:
                if t_walls[3] or t_walls[2]: #위, 왼쪽 확인
                    return False
                return True

    if t == 3:
        ny = y + dxys[t][idx][1]
        if 0 <= ny < c:
            t_walls = walls[x][ny]
            if idx == 0:
                if t_walls[3] or t_walls[1]: #위, 오른쪽
                    return False
                return True
            else:
                if t_walls[3] or t_walls[2]:  #위, 왼쪽
                    return False
                return True

    if t == 4:
        ny = y + dxys[t][idx][1]
        if 0 <= ny < c:
            t_walls = walls[x][ny]
            if idx == 0:
                if t_walls[4] or t_walls[1]: #아래, 오른쪽
                    return False
                return True
            else:
                if t_walls[4] or t_walls[2]: #아래, 왼쪽
                    return False
                return True

    return False

def init_heater():
    added_heater = [[0]*c for _ in range(r)]
    #모든 heater에 대해서 진행
    for x, y, t in heater:
        x += dxys[t][1][0]
        y += dxys[t][1][1]
        #heater 직방칸이 matrix범위를 나가는지 확인하기
        if not iscriteria(x,y):
            continue
        q = deque()
        # 5-1 부터 시작할 거임.
        q.append([x,y,4])
        global visited

        visited = [[False]*c for _ in range(r)]
        #heater 직방칸에 대해서 먼저 +5 해주기
        visited[x][y] = True
        added_heater[x][y] += 5

        #위, 아래 칸에 대해서 처리해주기
        while q:
            x, y, cnt = q.popleft()
            #3방향에 대해서 진행 for loop 3번 돎
            for idx, dxy in enumerate(dxys[t]):
                #이 부분이 중요!!
                #isnext로 x,y위치에서 t 방향으로 spread할 수 있는지 wall의 유무 확인하기
                if cnt > 0 and isnext(x, y, t, idx):
                    nx, ny = x + dxy[0], y + dxy[1]
                    if iscriteria(nx,ny) and not visited[nx][ny]:
                        added_heater[nx][ny] += cnt

                        q.append([nx,ny,cnt-1])
                        visited[nx][ny] = True
    return added_heater


def minus_one():
    for i in range(r):
        if maps[i][0] != 0:
            maps[i][0] -= 1
        if maps[i][-1] != 0:
            maps[i][-1] -= 1

    #위에서 계산한 내용을 반복하면 안됨. 그래서 range가 1, c-1임.
    for j in range(1, c-1):
        if maps[0][j] != 0:
            maps[0][j] -= 1
        if maps[-1][j] != 0:
            maps[-1][j] -= 1

def update_heater():
    global added_heater
    for i in range(r):
        for j in range(c):
            maps[i][j] += added_heater[i][j]

def spread_heat():
    #위, 오른쪽만 체크하는 방식임. 마지막 column은 위 체크, 마지막 row는 오른쪽 체크
    heats = [[0]*c for _ in range(r)]
    #조사하기 위함 r-1
    for x in range(r-1):
        nx = x + 1
        #조사하기 위함 c-1
        for y in range(c-1):
            #nx,y에 대해서
            if iscriteria(nx,y):
                #위에 벽이 없을 경우
                if not walls[nx][y][3]: #상
                    sub = abs(maps[nx][y]- maps[x][y])//4
                    if maps[nx][y] > maps[x][y]:
                        heats[nx][y] -= sub
                        heats[x][y] += sub
                    else:
                        heats[nx][y] += sub
                        heats[x][y] -= sub

            #오른쪽에 벽이 없을 경우
            #여기는 x,y에 대해서
            if not walls[x][y][1]: #우
                ny = y + 1
                sub = abs(maps[x][ny] - maps[x][y])//4
                if maps[x][ny] > maps[x][y]:
                    heats[x][ny] -= sub
                    heats[x][y] += sub
                else:
                    heats[x][ny] += sub
                    heats[x][y] -= sub

    y = c -1
    #위에서 처리하지 못한 마지막 column에 대해서
    for x in range(1, r):
        nx = x-1
        #위에 벽이 없을 경우
        if not walls[x][y][3]:
            sub = abs(maps[nx][y] - maps[x][y])//4
            if maps[nx][y] > maps[x][y]:
                heats[nx][y] -= sub
                heats[x][y] += sub
            else:
                heats[nx][y] += sub
                heats[x][y] -= sub

    x = r-1
    #위에서 처리하지 못한 마지막 row에 대해서 처리
    #마지막 row의 윗칸과의 처리도 해줘야 하지 않나???
    for y in range(1, c):
        ny = y-1
        #오른쪽에 벽이 있을 경우
        if not walls[x][ny][1]:
            sub = abs(maps[x][ny]- maps[x][y])//4
            if maps[x][ny] > maps[x][y]:
                heats[x][ny] -= sub
                heats[x][y] += sub
            else:
                heats[x][ny] += sub
                heats[x][y] -= sub


    #map update해주기
    for x in range(r):
        for y in range(c):
            maps[x][y] += heats[x][y]

    minus_one()

def cnt_choc():
    for x, y in checked_pos:
        if maps[x][y] < k:
            return False
    return True

visited = [[False]*c for _ in range(r)]
cnt = 1
#1단계를 다시 반복하게 되더라도 똑같은 값의 update가 이뤄져야 함. 그래서 그 값을 added_heater에 미리 저장해두고
#update_heater에서 더해준다
added_heater = init_heater()
while cnt <= 100:
    update_heater()
    spread_heat()
    if cnt_choc():
        break
    cnt += 1
print(cnt)