import sys
from collections import deque
from copy import deepcopy
import heapq
input = sys.stdin.readline

M, S = map(int,input().split())
fish_list = []

ocean = [[[] for _ in range(4)] for _ in range(4)]
init = [[[] for _ in range(4)] for _ in range(4)]
# print(init)
#print(ocean)

#복제를 위해 init 따로 만들기
for i in range(M):
    x, y, d = map(int,input().split())
    init[x-1][y-1].append(d-1)

sharkx, sharky = map(int,input().split())
sharkx -= 1
sharky -= 1

#fish smell matrix 만들기
smell = [[0]*4 for _ in range(4)]

def magic_trial(tmp):
    for i in range(4):
        for j in range(4):
            for x in range(len(tmp[i][j])):
                ocean[i][j].append(tmp[i][j][x])

def next_fish_move(x,y,d):
    global smell, sharkx, sharky
    fish_direction = [(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]
    for i in range(d, d-8, -1):
        #modulus사용하기
        i %= 8
        nx = x + fish_direction[i][0]
        ny = y + fish_direction[i][1]
        print(i)
        #matrix 범위, smell, 상어 위치 체크
        if 0 <= nx < 4 and 0<= ny < 4 and smell[nx][ny] == 0 and (nx,ny)!= (sharkx,sharky):
            return nx, ny, i

    return x, y, d

def fish_swim():
    global smell
    #fish_direction = [(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]
    tmp_fish_moved = [[[]for _ in range(4)]for _ in range(4)]
    for i in range(4):
        for j in range(4):
            #물고기가 존재한다면
            x,y = i,j
            if len(ocean[x][y]) > 0:
                #list에 있는 모든 물고기에 대해서
                #복제 기능때문에 한곳에 많은 물고기 존재 가능함...!!
                for f in ocean[x][y]:
                    nx, ny, dir = next_fish_move(x,y,f)
                    tmp_fish_moved[nx][ny].append(dir)
                    #if (nx,ny) != (x,y):
                    #    tmp_fish_moved[nx][ny].append(dir)

    for i in range(4):
        for j in range(4):
            ocean[i][j] = tmp_fish_moved[i][j]

def dictionary_level(moves):
    global candidate_moves
    changed = ''
    for i in moves:
        changed += str(i)

    heapq.heappush(candidate_moves, int(changed))

def shark_swim(x, y, move_list, fish_caught, visited):
    global final_caught, candidate_moves, direction, sharkx, sharky
    # if len(fish_map[sharkx][sharky])>0:
    #     fish_caught += len(fish_map[sharkx][sharky])
    #     fish_map[sharkx][sharky] = []

    if len(move_list) == 3:
        #fish 개수 비교
        if fish_caught > final_caught:
            final_caught = fish_caught
            candidate_moves = move_list[:] #어차피 사전순임.
            # candidate_moves = []
            # dictionary_level(move_list)

        # elif fish_caught == final_caught:
        #     dictionary_level(move_list)
        return

    for i in range(4):
        nx = direction[i][0] + x
        ny = direction[i][1] + y

        #matrix 범위 체크
        if 0<=nx<4 and 0<=ny<4:
            #방문했던 곳을 또 방문해도됨. 먹지만 않으면 됨.
            if not visited[nx][ny]:
                visited[nx][ny] = True
                shark_swim(nx, ny, move_list + [i], fish_caught+ len(ocean[nx][ny]), visited)
                visited[nx][ny] = False
            else:
                shark_swim(nx,ny, move_list+[i], fish_caught, visited)



def decode_dictionary(moves):
    tmp = []
    for m in str(moves):
        tmp.append(int(m))
    return tmp

def update_ocean(candidate_moves):
    global direction, sharkx, sharky
    #move = decode_dictionary(candidate_moves)
    for m in candidate_moves:
        nx = direction[m][0] + sharkx
        ny = direction[m][1] + sharky

        if len(ocean[nx][ny]) > 0:
            #여기서 += 3이 아님. 그냥 3임. 먹힌 장소를 또 먹을 수 없기 때문.
            smell[nx][ny] = 3

            #fish kill
            ocean[nx][ny] = []

        sharkx, sharky = nx, ny

def erase_smell():
    global smell
    for i in range(4):
        for j in range(4):
            if smell[i][j] > 0:
                smell[i][j] -= 1

def calculate_fish():
    total = 0
    for i in range(4):
        for j in range(4):
            if len(ocean[i][j]) != 0:
                total += len(ocean[i][j])

    return total


direction = [(-1,0),(0,-1),(1,0),(0,1)] #상, 좌, 하, 우
count = 0
magic_trial(init)

while True:
    candidate_moves = [] #heapq로 사용하기
    #사전순 비교를 고려해서 -1로 해줘야함. final caught이 0이더라도 사전순으로 작은 것을 골라야 하기 때문에 shart route를 찾는 것이 목표이기 떄문.
    final_caught = -1
    #복제 map은 이전에 나온 ocean 결과임!!
    init = deepcopy(ocean)
    fish_swim()

    # erase_smell()

    #print('after swim', ocean)
    ####상어 위치에 물고기가 존재할 경우 상관없음. 그냥 add해주면 됨.
    visited = [[False]*4 for _ in range(4)]
    #어차피 0~4까지 돌기 때문에 사전순임.
    #여기서 candidate_moves를 찾는거임.
    shark_swim(sharkx,sharky, [], 0, visited)

    #candidate_moves = heapq.heappop(candidate_moves)

    update_ocean(candidate_moves)
    erase_smell()

    magic_trial(init)

    count += 1

    if count == S:
        break

print(calculate_fish())