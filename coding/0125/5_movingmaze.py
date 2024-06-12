#bfs
#queue사용하기

import sys
sys.stdin = open('./0125/5_movingmaze.txt')

#input
matrix = []
for _ in range(8):
    matrix.append(list(map(str, input())))

#9가지 체크
dx = [0,0,-1,1,]
dy = [1,-1,0,0,]

def bfs(position_x, position_y, matrix):
    queue = [(position_x, position_y)]

    while queue:
        currentx, currenty = queue.pop(0)
        for i in range(9):



#시간이 지날때마다 움직이는 벽을 어떻게 표현하지?