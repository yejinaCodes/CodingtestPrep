n = int(input())
cube = dict()

def init():
    cube['U'] = [['w' for _ in range(3)] for _ in range(3)]
    cube['D'] = [['y' for _ in range(3)] for _ in range(3)]
    cube['F'] = [['r' for _ in range(3)] for _ in range(3)]
    cube['B'] = [['o' for _ in range(3)] for _ in range(3)]
    cube['L'] = [['g' for _ in range(3)] for _ in range(3)]
    cube['R'] = [['b' for _ in range(3)] for _ in range(3)]


def rotate_90(board):
    new_board = [['k' for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            new_board[i][j] = board[3-j-1][i]
    return new_board
def get_vertical(_type, h):
    tmp = []
    for i in range(3):
        tmp.append(cube[_type][i][h])
    return tmp

def set_vertical(_type, h, data):
    for i in range(3):
        cube[_type][i][h] = data[i]

def turn_u():
    cube['U'] = rotate_90(cube['U'])

    left = get_vertical('L',2)[::-1] #넣어줄때 거꿀로 넣어줘야 하기 때문

    front = cube['F'][0]
    set_vertical('L',2,front) #이건 그대로 넣어주면 됨

    right = get_vertical('R', 0)[::-1]
    cube['F'][0] = right

    back = cube['B'][2]
    set_vertical('R', 0, back)

    cube['B'][2] = left

    return

def turn_d():

    cube['D'] = rotate_90(cube['D'])

    left = get_vertical('L',0)

    back = cube['B'][0][::-1]
    set_vertical('L',0,back)

    right = get_vertical('R',2)
    cube['B'][0] = right

    front = cube['F'][2][::-1]
    set_vertical('R',2,front)

    cube['F'][2] = left

    return

def turn_f():
    cube['F'] = rotate_90(cube['F'])

    left = cube['L'][2]

    down = cube['D'][0][::-1]
    cube['L'][2] = down

    right = cube['R'][2][::-1]
    cube['D'][0] = right

    up = cube['U'][2]
    cube['R'][2] = up

    cube['U'][2] = left

    return

def turn_b():
    cube['B'] = rotate_90(cube['B'])

    left = cube['L'][0][::-1]

    up = cube['U'][0]
    cube['L'][0] = up

    right = cube['R'][0]
    cube['U'][0] = right

    down = cube['D'][2][::-1]
    cube['R'][0] = down

    cube['D'][2] = left

    return

def turn_r():
    cube['R'] = rotate_90(cube['R'])

    up = get_vertical('U', 2)

    front = get_vertical('F',2)
    set_vertical('U',2,front)

    down = get_vertical('D',2)
    set_vertical('F',2,down)

    back = get_vertical('B',2)
    set_vertical('D',2,back)

    set_vertical('B',2,up)

    return

def turn_l():
    cube['L'] = rotate_90(cube['L'])

    down = get_vertical('D',0)

    front = get_vertical('F',0)
    set_vertical('D', 0,front)

    up = get_vertical('U',0)
    set_vertical('F',0,up)

    back = get_vertical('B',0)
    set_vertical('U',0,back)

    set_vertical('B',0,down)

    return


for _ in range(n):
    turn = int(input())
    order = list(input().split())
    init()

    for k in range(turn):
        turn_type, rotate_d = order[k]
        rotate = 1
        if rotate_d == '-':
            rotate = 3

        if turn_type == 'U':
            for _ in range(rotate):
                turn_u()

        if turn_type == 'D':
            for _ in range(rotate):
                turn_d()

        if turn_type == 'F':
            for _ in range(rotate):
                turn_f()

        if turn_type == 'B':
            for _ in range(rotate):
                turn_b()

        if turn_type == 'L':
            for _ in range(rotate):
                turn_l()

        if turn_type == 'R':
            for _ in range(rotate):
                turn_r()

    #back이 이미 윗부분임. 그래서 그냥 row로 출력하면 됨.
    for i in range(3):
        print(''.join(cube['U'][i]))
