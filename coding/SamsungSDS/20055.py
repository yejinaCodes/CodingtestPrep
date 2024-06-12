import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
conveyor_belt = deque(map(int, input().split()))
robots_position = deque()
current_positions = [False for _ in range(len(conveyor_belt))]

count = 1

def belt_rotate():
    tmp = conveyor_belt.pop()
    conveyor_belt.appendleft(tmp)
    for robot in robots_position:
        current_positions[robot] = False
        robot += 1
        if robot == len(conveyor_belt):
            robot = 0
        current_positions[robot] = True

def robot_move():
    for robot in robots_position:
        if robot == len(conveyor_belt) - 1:
            tmp = 0
        else:
            tmp = robot + 1
        if conveyor_belt[tmp] == 0:
            continue
        elif current_positions[tmp] == True:
            continue
        #움직일 수 있다면 robot 옮기기
        conveyor_belt[tmp] -= 1
        current_positions[tmp] = True
        current_positions[robot] = False
        robot = tmp

def check_k():
    tmp = conveyor_belt.count(0)
    if tmp >= K:
        return True

need_to_place = N

#첫번째 로봇 올리기
robots_position.append(0)
current_positions[0] = True
conveyor_belt[0] -= 1
need_to_place -= 1

while True:
    belt_rotate()
    count += 1
    robot_move()
    count += 1

    #올리는 위치에 로봇도 없어야 함. 각 칸에 로봇 하나밖에 없어야 함.
    if need_to_place > 0 and conveyor_belt[0] > 0 and current_positions[0] == False:
        #벨트 위에 로봇을 올린다
        robots_position.append(0)
        current_positions[0] = True
        conveyor_belt[0] -= 1
        need_to_place -= 1
    count += 1

    if check_k():
        break

print(count)



        


