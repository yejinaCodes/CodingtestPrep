import sys
input = sys.stdin.readline

#input 받기
R,C,M = map(int,input().split())
sharks = []

#sharks의 정보 track하기
map_ = [[0]*(C+1) for _ in range(R+1)]

for i in range(M):
    r,c,speed,direction,size = map(int,input().split())
    sharks.append((r,c,speed,direction,size))
    map_[r][c] = size

#print(map_)
result = 0
def fishing(column):
    global map_, sharks, result
    #모든 column보기
    for i in range(1, R+1):
        tmp = map_[i][column]
        if tmp > 0:
            result += tmp
            map_[i][column] = 0
            return         
    return

move = [(-1,0),(1,0),(0,1),(0,-1)] #위,아래,오른쪽, 왼쪽

def shark_move(shark, tmp, count): 
    x,y, speed, direction, size = shark

    if count == speed:
    #이미 tmp 해당 위치에 존재할 경우 size로 비교하고 작은 상어 지워주기
        #먹힌거 어떻게 제거하지?
        if tmp[x][y] == 0 or size > tmp[x][y]:
            tmp[x][y] = size
            sharks.append(shark)
            return 
        elif size < tmp[x][y]:
            return

    #move 계산하기
    nx = x + move[direction-1][0]
    ny = y + move[direction-1][1]

    #direction바꿔주기
    if nx>R:
        direction = 0
        shark_move(shark, tmp, count)
    elif nx<=0:
        direction = 1
        shark_move(shark, tmp, count)
    elif ny>C:
        direction = 2
        shark_move(shark, tmp, count)
    elif ny<=0:
        direction = 3
        shark_move(shark, tmp, count)
    else:
        x, y = nx, ny
        count += 1
        shark_move(shark, tmp, count)
    

#낚시왕 오른쪽으로 한칸씩 이동함
for column in range(1,C+1):
    fishing(column)
    tmp = [[0]*(C+1) for _ in range(R+1)]
    for shark in sharks:

        sharks.pop(sharks.index(shark))
        shark_move(shark, tmp,0)
    

print(result)







                    # if direction == 1: #up
                    #     if tmpi == 1:
                    #     #if tmpi - 1 < 1:

                    #         direction = 2
                    #         tmpi = tmpi + 1 
                    #     else:
                    #         tmpi = tmpi -1

                    # elif direction == 2: #down
                    #     if tmpi == R:
                    #     #if tmpi + 1 > R:
                    #         direction = 1
                    #         tmpi = tmpi - 1
                    #     else:
                    #         tmpi = tmpi + 1 
                    # elif direction == 3: #right
                    #     if tmpj == C:
                    #     #if tmpj + 1 > C:
                    #         direction = 4
                    #         tmpj = tmpj - 1
                    #     else:
                    #         tmpj = tmpj + 1
                    # elif direction == 4: #left
                    #     if tmpj == 1:
                    #     #if tmpj - 1 < 1:
                    #         direction = 3
                    #         tmpj = tmpj + 1
                    #     else:
                    #         tmpj = tmpj - 1