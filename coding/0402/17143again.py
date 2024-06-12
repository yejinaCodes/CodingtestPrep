import sys
input = sys.stdin.readline

#input
R,C,M = map(int,input().split())
map_ = [[[] for _ in range(C)] for _ in range(R)]
#print(map_)
for i in range(M):
    r,c,speed,direction,size = map(int,input().split())
    map_[r-1][c-1] = [speed,direction-1,size]
    #print(speed, direction, size)

#print(map_)
caught = 0

def fishing(column):
    #global map_
    global caught
    for i in range(R):
        #상어찾음
        if map_[i][column]:
            caught += map_[i][column][2]
            map_[i][column] = []
            print(caught)
            break
            #return s
    #return 0

#상 하 우 좌
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

#상어 움직이기
def shark_move():
    #global map_
    tmp = [[[] for _ in range(C)] for _ in range(R)]
    #print(tmp)
    for i in range(R):
        for j in range(C):
            if map_[i][j]:
                #print(map_[i][j])
                speed, direction, size = map_[i][j][0], map_[i][j][1], map_[i][j][2]
                tmpi, tmpj = i,j
                for _ in range(speed):
                    #print(direction)
                    nx = tmpi + dx[direction]
                    ny = tmpj + dy[direction]

                    if nx < 0 or nx >= R or ny < 0 or ny >= C:
                        if direction == 0: #상
                            direction = 1
                        elif direction == 1: #하
                            direction = 0
                        elif direction == 2:
                            direction = 3
                        elif direction == 3:
                            direction = 2

                        nx = tmpi + dx[direction]
                        ny = tmpj + dy[direction]

                    tmpi, tmpj = nx, ny

                tmp[tmpi][tmpj].append([speed, direction, size])


    for i in range(R):
        for j in range(C):
            if len(tmp[i][j]) == 0:
                continue
            #if len(tmp) > 1:
            else:
                tmp[i][j].sort(reverse=True)
                tmp[i][j] = tmp[i][j][0]     

    return tmp

#낚시왕의 fishing
for column in range(C):
    fishing(column)
    #caught += fishing(column)
    map_ = shark_move()

print(caught)