#최대 5번의 이동이 있음
#각 이동에는 4번의 방향이 존재 
#모든 경우의 수는 = ?가지 존재? 계산하는 방법 익히기
#4^5경우

import sys
input = sys.stdin.readline
from copy import deepcopy

N = int(input())
game_board = [list(map(int,input().split())) for _ in range(N)]

directions = [(-1,0),(0,1), (1,0), (0,-1)] #위, 오른쪽, 아래, 왼쪽

def move(gameboard, direction):
    #위일때
    if direction == 0:

    #오른쪽일때
    elif direction == 1:
        tmp = []
        for row in gameboard:
            for x in range(N):
                if row[x] == 0:
                    continue
                else:
                    tmp.append(row[x])

    #아래일때
    elif direction == 2:

    #왼쪽일때
    elif direction == 3:
        tmp = []
        for row in gameboard:
            for x in range(N):
                if row[x] == 0:
                    continue
                else:
                    tmp.append(row[x])
            

    

def collect():




result = 0

def backtracking(gameboard, count):

    if count > 5:
        result = max(result, max(gameboard))
        return
    for i in range(4):
        move(gameboard,i)
        collect(gameboard, i)
        backtracking(deepcopy(gameboard), i)


backtracking(game_board, 0)

# for _ in range(5):
#     for i in range(4):
#         x, y = directions[i]
#         backtracking(deepcopy(game_board), x,y)



# def backtracking(map_, dir, biggest):

#     if dir == 0:


#     elif dir == 1:

#     elif dir == 2:

#     elif dir == 3:


# for i in range(4):
#     backtracking(game_board, i, biggest_block)
