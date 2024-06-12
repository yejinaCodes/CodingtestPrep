import sys 
input = sys.stdin.readline

R,C,M = map(int,input().split())

sharks = []
for i in range(M):
    sharks.append(list(map(int,input().split())))

map_ = [[[]for _ in range(C)] for _ in range(R)]

for i in range(len(sharks)):
    map_[sharks[i][0]-1][sharks[i][1]-1] = [sharks[i][4], sharks[i][2], sharks[i][3]-1]
    #map_[i[0]-1][i[1]-1].append([i[2], i[3], i[4]])
#print(map_)
caught = 0

def fishing(column):
    global caught
    for i in range(R):
        #값이 없을 경우
        if len(map_[i][column]) == 0:
            continue
        else:
            caught += map_[i][column][0]
            map_[i][column] = []
            break
        #값이 있을 경우
        # if map_[i][column]:
        #     caught += map_[i][column][0]
        #     map_[i][column] = []
        #     break

#상하우좌
dx = [-1,1,0,0]
dy = [0,0,1,-1]

def shark_move():
    global map_
    tmp_map = [[[]for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if map_[i][j]:
                x,y = i,j
                size, speed, direction = map_[i][j][0], map_[i][j][1], map_[i][j][2]
                for _ in range(speed):
                    nx = dx[direction] + x
                    ny = dy[direction] + y
                    #벗어날 경우
                    if nx<0 or nx>=R or ny<0 or ny>=C:
                        if direction == 0: #위일 경우
                            direction = 1
                        elif direction == 1:
                            direction = 0
                        elif direction == 2:
                            direction = 3
                        elif direction == 3:
                            direction = 2
                        nx = dx[direction] + x
                        ny = dy[direction] + y
                    
                    x,y = nx, ny
                tmp_map[x][y].append([size,speed,direction])
                    
    
    #check 
    for i in range(R):
        for j in range(C):
            if len(tmp_map[i][j]) == 0:
                continue
            if len(tmp_map) > 1:
                tmp_map[i][j].sort(reverse=True)
                tmp_map[i][j] = tmp_map[i][j][0]

    return tmp_map


for column in range(C):
    fishing(column)
    map_ = shark_move()

print(caught)