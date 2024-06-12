import sys
#sys.stdin = open("input.txt", "r")
from collections import deque
from copy import deepcopy

dx = [-1, 1, 0, 0]  # 상 하 좌 우
dy = [0, 0, -1, 1]

def check_direction(d,x,y,xynos,powercnt):
    #print('in', x,y)
    tmp = deepcopy(xynos)
    while True:
    #for i in range(7):
        x = dx[d] + x
        y = dy[d] + y
        #print('process:', x,y)
        # if x < 0:
        #     print(x,y).
        #print(x,y)
        if x < 0 or x >= N or y < 0 or y >= N:
            #print(x,y)
            return tmp, powercnt

        elif tmp[x][y] == 1:
            return xynos, 0

        powercnt += 1
        tmp[x][y] = 1
        # else:
        #     powercnt += 1
        #     xynos[x][y] = 1
    #print('returning', powercnt)
    #return tmp, powercnt


def backtracking(xynos, core, powerline, core_count):
    global final_core_cnt, final_powerline
    pc = deepcopy(xynos)
    pcore = deepcopy(core)
    if len(core) == 0:
        #print(core_count, powerline)
        if core_count > final_core_cnt:
            final_core_cnt = core_count
            final_powerline = powerline
        #같을 경우 전선 길이 합이 최소가 되는 것을 고르기
        elif core_count == final_core_cnt:
            if powerline < final_powerline:
                final_powerline = powerline
        return

    cur_core_x, cur_core_y = pcore.popleft()
    #4가지 방향 체크하기
    for i in range(4):
        #가장자리임
        if cur_core_x == 0 or cur_core_y == 0:
            backtracking(pc, deepcopy(pcore), powerline, core_count + 1)
            break

        pc, powercnt = check_direction(i, cur_core_x, cur_core_y, pc, 0)
        #print('checking', powercnt)
        #print('powerline', powerline)
        #sys.exit()
        if powercnt == 0: #전선이 연결되지 못했을 경우
            backtracking(pc, deepcopy(pcore), powerline, core_count)
        else: #전선을 연결했을 경우
            backtracking(pc, deepcopy(pcore), powerline+powercnt, core_count + 1)


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())

    xynos = []
    for i in range(N):
        xynos.append(list(map(int,input().split())))

    final_core_cnt = -1
    final_powerline = 1e9

    core = deque()

    for i in range(N-1):
        for j in range(N-1):
            if xynos[i][j] == 1:
                core.append((i,j))
    # for i in range(N):
    #     for j in range(N):
    #         backtracking(i,j,xynos,0,0)

    backtracking(xynos,core,0,0)

    #모든 core이 가장자리에 있을 경우
    if final_powerline == 1e9:
        final_powerline = 0

    print('#', test_case, ' ', final_powerline)






