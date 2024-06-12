import sys
from collections import deque
from copy import deepcopy

# 각 면의 위,오른쪽,아래,왼쪽의 닿는 면 리스트 사용
side_directions = {'F': ['U', 'R', 'D', 'L'], 'R': ['U', 'B', 'D', 'F'], 'L' : ['U', 'F', 'D', 'B'],
                   'U': ['L','B', 'R', 'F'], 'D': ['F', 'R', 'B', 'L'], 'B': ['U', 'L', 'D', 'R']}

def get_moving(prev_side_order,side):
    global entire_cube
    tmp = []
    #예. U side가지고 와서 F side와 닿는 부분 tmp에 저장하기
    order = side_directions.get(prev_side_order)
    position = -1
    for i in range(4):
        if order[i] == side:
            position = i
            break

    one_side = entire_cube.get(prev_side_order)

    #첫번째 row일 경우
    if position == 0:
        for p in range(3):
            tmp.append(one_side[0][p])
    #마지막 column
    elif position == 1:
        for p in range(3):
            tmp.append(one_side[p][2])
    #마지막 row
    elif position == 2:
        for p in range(3):
            tmp.append(one_side[2][p])
    #첫번째 column
    elif position == 3:
        for p in range(3):
            tmp.append(one_side[p][0])
    return tmp

def insert_color(new_side_order, side, floating):
    global entire_cube
    tmp = []

    order = side_directions.get(new_side_order)
    position = -1
    #order list에서 몇번째 idx인지 찾기
    for i in range(4):
        if order[i] == side:
            position = i
            break

    one_side = entire_cube.get(new_side_order)

    #값 바꿔주기
    #first row
    if position == 0:
        for p in range(3):
            tmp.append(one_side[0][p])
            one_side[0][p] = floating[p]
    #last column
    elif position == 1:
        for p in range(3):
            tmp.append(one_side[p][2])
            one_side[p][2] = floating[p]
    #last row
    elif position == 2:
        for p in range(3):
            tmp.append(one_side[2][p])
            one_side[2][p] = floating[p]
    #first column
    elif position == 3:
        for p in range(3):
            tmp.append(one_side[p][0])
            one_side[p][0] = floating[p]

    return tmp


def getUpper():
    global entire_cube, final
    tmp2 = []
    upper_side = entire_cube.get('U')

    #마지막 column부터 첫번째까지
    for j in range(2,-1,-1):
        tmp = ''
        for i in range(3):
            tmp += upper_side[i][j]

        tmp2.append(tmp)
    final = tmp2

T = int(input())
for testcase in range(T):
    times = int(input())
    final = []
    equation = list(input().split())

    # 각 면을 뜻하는 matrix 초기화
    entire_cube = {'F': [['r'] * 3 for _ in range(3)], #front
                   'R': [['b'] * 3 for _ in range(3)], #right
                   'L': [['g'] * 3 for _ in range(3)], #left
                   'U': [['w'] * 3 for _ in range(3)], #upper
                   'D': [['y'] * 3 for _ in range(3)], #down
                   'B': [['o'] * 3 for _ in range(3)]} #back

    #print(times)
    for i in range(times):

        #예) F+
        side, rotate = equation[i][0], equation[i][1]

        direction = side_directions.get(side)
        tmp_dir = deque(deepcopy(direction))
        #바뀐 순서 만들어주기
        if rotate == "+":
            x = tmp_dir.popleft()
            tmp_dir.append(x)
        else:
            x = tmp_dir.pop()
            tmp_dir.appendleft(x)

        floating = []
        #한 면씩 바꿔주기
        if rotate == "+":
            for step in range(4):
                # prev-> new로 옮겨줘야 함.
                #예. U->R로
                prev_side_order = direction[step]
                new_side_order = tmp_dir[step]

                # prev 에서 해당 side와 닿아있는 면의 값 가지고 오기
                if step == 0:
                    tmp = get_moving(prev_side_order, side)
                    # 가지고 온 값을 넣어주기
                    tmp2 = insert_color(new_side_order, side, tmp)
                    floating = tmp2
                else: #이전 move 에서 tmp에 저장한 값을 사용해야 함.
                    tmp2 = insert_color(new_side_order, side, floating)
                    floating = tmp2

        elif rotate == "-":
            #순서가 역방향이기 때문
            for step in range(3,-1,-1):
                # prev-> new로 옮겨줘야 함.
                # 예. U->R로
                prev_side_order = direction[step]
                new_side_order = tmp_dir[step]

                # prev 에서 해당 side와 닿아있는 면의 값 가지고 오기
                if step == 3:
                    tmp = get_moving(prev_side_order, side)
                    # 가지고 온 값을 넣어주기
                    tmp2 = insert_color(new_side_order, side, tmp)
                    floating = tmp2
                else:  # 이전 move 에서 tmp에 저장한 값을 사용해야 함.
                    tmp2 = insert_color(new_side_order, side, floating)
                    floating = tmp2

        #Upper matrix를 3,2,1 column순서로 string으로 변환해서 final 에 넣기
        getUpper()


        print(i)
        #각 letter equation이 끝난뒤 upper 결과 값 확인하기
        for x in range(3):
            #for y in range(3):
            print(entire_cube.get('U')[x])



    #모든 결과 출력
    for i in final:
        print(i)
