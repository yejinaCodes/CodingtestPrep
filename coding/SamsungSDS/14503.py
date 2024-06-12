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
        #search할때부터 왼쪽 방향으로 서치하기!!
        #d = (d+3) % 4
        #방향이 0, 1, 2, 3 이렇게 총 4개다.
        #그리고 왼쪽으로 돌리면 3, 2, 1, 0 요렇다.

        #빈칸이 나올수 있는지 반시계방향으로 먼저확인하기
        robotd = (robotd+3)%4
        #robotd = rotate_robot.get(robotd)
        nx = dx[robotd] + robotx
        ny = dy[robotd] + roboty

        #청소 가능하다면
        #청소했던 곳은 이미 청소된곳이라서 청소 가능한 곳이 아님
        if 0 <= nx < N and 0 <= ny < M and room[nx][ny] == 0:
            if visited[nx][ny] == False:
                visited[nx][ny] = True
                count += 1
                robotx, roboty = nx, ny
                flag = True
                break
    #4방향 모두 청소할 수 없을 때
    if not flag:
        if room[robotx - dx[robotd]][roboty - dy[robotd]] == 1:
            break
        else:
            robotx, roboty = robotx - dx[robotd], roboty - dy[robotd]

    #
    #     #현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
    #     if room[nx][ny] == 0:
    #         flag = True
    #         break
    #
    # #현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우:
    # if not flag:
    #     back = check_back.get(robotd)
    #     # 후진 할 수 없는 경우:
    #     if room[dx[back] + x][dy[back] + y] == 1:
    #         break
    #     # 후진 할 수 있는 경우:
    #     else:
    #         q.append((dx[back] + x, dy[back] + y))
    # #빈 칸이 있는 경우:
    # if flag:
    #     robotd = rotate_robot.get(robotd)
    #     if room[dx[robotd] + x][dy[robotd] + y] == 0:
    #         q.append((dx[robotd] + x, dy[robotd] + y))
    #

print(count)