import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
robotx, roboty, robotd = map(int, input().split())

room = []

for i in range(N):
    room.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0] #상우하좌
dy = [0, 1, 0, -1]

# q = deque()
# q.append((robotx, roboty))

#(d+3)%4
rotate_robot = {0:3, 3:2, 2:1, 1:0}
check_back = {0:2, 1:3, 2:0, 3:1}

visited = [[False] * M for _ in range(N)]

visited[robotx][roboty] = True
count = 1

while True:
    flag = False
    #현재 칸의 주변 4칸 체크하기
    for _ in range(4):
        robotd = rotate_robot.get(robotd)
        nx = dx[robotd] + robotx
        ny = dy[robotd] + roboty

        #현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
        if room[nx][ny] == 0:
            flag = True
            robotx, roboty = nx, ny
            count += 1
            break


    #현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우:
    if not flag:
        back = check_back.get(robotd)
        # 후진 할 수 없는 경우:
        if room[dx[back] + robotx][dy[back] + roboty] == 1:
            break
        # 후진 할 수 있는 경우:
        else:
            robotx, roboty = dx[back] + robotx, dy[back] + roboty
    #빈 칸이 있는 경우:
    # if flag:
    #     if room[dx[robotd] + robotx][dy[robotd] + roboty] == 0:
    #     robotx, roboty = dx[robotd] + robotx, dy[robotd] + roboty


print(count)