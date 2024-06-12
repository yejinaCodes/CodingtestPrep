#벽을 어떻게 표현할지가 중요함
import sys
from collections import deque
input = sys.stdin.readline

R,C,K = map(int,input().split())
room = []
chocolate = 0
for i in range(R):
    room.append(list(map(int,input().split())))

Walls = int(input())
vertical_wall = {}
horizontal_wall = {}

for i in range(Walls):
    tmp = list(map(int,input().split()))
    if tmp[-1] == 0:
        horizontal_wall[(tmp[0]-1,tmp[1]-1)] = (tmp[0]-2, tmp[1]-1)
        horizontal_wall[(tmp[0]-2, tmp[1]-1)] = (tmp[0]-1, tmp[1]-1)
    elif tmp[-1] == 1:
        vertical_wall[(tmp[0]-1,tmp[1]-1)] = (tmp[0]-1, tmp[1])
        vertical_wall[(tmp[0]-1, tmp[1])] = (tmp[0]-1, tmp[1]-1)
#print(vertical_wall)
# if (3,4) not in vertical_wall.keys():
#     print('yes')

#온풍기 위치 저장
heaters = []
speculation_area = []
for i in range(R):
    for j in range(C):
        if room[i][j] == 0:
            continue
        if room[i][j] == 5:
            speculation_area.append((i,j))
        else:
            heaters.append((i,j,room[i][j]))
# print(speculation_area)

def temperature():
    dir = [(0,1),(0,-1),(-1,0),(1,0)] #우좌상하
    tmp = [[0]*C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            x,y = i,j
            for z in range(4):
                nx = dir[z] + x
                ny = dir[z] + y

                if R<=nx<0 or C<=ny<0:
                    continue
                if check_wall(nx,ny,z):
                    continue

                diff = (room[i][j]-room[nx][ny])//4
                if room[i][j] > room[nx][ny]:
                    tmp[i][j] -= diff
                    tmp[nx][ny] += diff
                else:
                    tmp[i][j] += diff
                    tmp[nx][ny] -= diff
    #room update
    for i in range(R):
        for j in range(C):
            room[i][j] += tmp[i][j]

def outlier():
    #벽도 고려해야 하나?
    for j in range(C):
        if room[0][j] != 0:
            room[0][j] -= 1
        if room[R-1][j] != 0:
            room[R-1][j] -= 1
    for i in range(R):
        if room[i][0] != 0:
            room[i][0] -= 1
        if room[i][C-1] != 0:
            room[i][C-1] -= 1
def check_wall(x,y, d):
    #방향에 따라 vertical, horizontal 체크한다?
    if d == 0: #오른쪽에서 온거임
        #값이 존재한다면
        if (x,y) in horizontal_wall.keys() and horizontal_wall[(x,y)] == (x-1,y): #위
            return True
        elif (x,y) in vertical_wall.keys() and vertical_wall[(x,y)] == (x,y+1): # 옆
            return True
        elif (x,y) in horizontal_wall.keys() and horizontal_wall[(x,y)] == (x+1,y): #아래
            return True

    elif d == 1: #왼쪽에서 온거임
        #값이 존재한다면
        if (x,y) in horizontal_wall.keys() and horizontal_wall[(x,y)] == (x-1,y): #위
            return True
        elif (x,y) in vertical_wall.keys() and vertical_wall[(x,y)] == (x,y-1): # 옆
            return True
        elif (x,y) in horizontal_wall.keys() and horizontal_wall[(x,y)] == (x+1,y): #아래
            return True

    elif d == 2: #위에서 온거임
        if (x,y) in vertical_wall.keys() and vertical_wall[(x,y)] == (x,y-1):
            return True
        elif (x,y) in horizontal_wall.keys() and horizontal_wall[(x,y)] == (x-1,y):
            return True
        elif (x,y) in vertical_wall.keys() and vertical_wall[(x,y)] == (x,y+1):
            return True

    elif d == 3: #아래에서 온거임
        if (x,y) in vertical_wall.keys() and vertical_wall[(x,y)] == (x,y-1):
            return True
        elif (x,y) in horizontal_wall.keys() and horizontal_wall[(x,y)] == (x+1,y):
            return True
        elif (x,y) in vertical_wall.keys() and vertical_wall[(x,y)] == (x,y+1):
            return True


def blow_wind(heater):
    direction = [(0,1),(0,-1),(-1,0),(1,0)]
    sp_direction = [[(-1,1),(0,1),(1,1)],[(-1,-1),(0,-1),(1,-1)],[(-1,-1),(-1,0),(-1,1)],[(1,-1),(1,0),(1,1)]]

    tmp_room = [[0]*(C) for _ in range(R)]
    x,y,d = heater
    d -= 1
    start = 5
    #첫번째 직방칸은 5 상승
    nx, ny = x+direction[d][0], y+direction[d][1]
    tmp_room[nx][ny] = start

    area = deque()
    area.append((nx,ny))

    visited = [[False]*C for _ in range(R)]
    #이후 spread
    while start > 1:
        if len(area) == 0:
            break
        x, y = area.popleft()
        start -= 1
        #방향 확인
        for i in range(3):
            nx = sp_direction[d][i][0] + x
            ny = sp_direction[d][i][1] + y

            #벗어날 경우
            if nx < 0 or nx >= R or ny < 0 or ny >= C or visited[nx][ny]:
                continue

            #벽이 있을 경우
            if check_wall(nx,ny,d):
                continue

            tmp[nx][ny] += start
            visited[nx][ny] = True
            area.append((nx,ny))

    #room 업데이트 해주기
    for i in range(R):
        for j in range(C):
            room[i][j] += tmp_room[i][j]

    return


while True:
    flag = False
    if chocolate >= 100:
        print(101)
        sys.exit()

    for i in range(len(speculation_area)):
        x,y = speculation_area[i]
        if room[x][y] < K:
            flag = True

    if not flag:
        print(chocolate)
        sys.exit()

    #모든 온풍기는 blow_wind 한다
    for i in range(len(heaters)):
        blow_wind(heaters[i])

    temperature()
    outlier()
    chocolate += 1
