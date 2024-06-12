import sys
from collections import deque
input = sys.stdin.readline

home = []
robot_loc = []
amount = 0
r,c,time = map(int,input().split())
for i in range(r):
    home.append(list(map(int,input().split())))

tmp_home = [[0]*c for i in range(r)]
#print(tmp_home)

dx = [0,0,-1,1] #우좌위아래
dy = [1,-1,0,0]

def calculatevirus(i,j):
    num = home[i][j]//5
    if num == 0:
        return
    count = 0
    for x in range(4):
        nx = i + dx[x]
        ny = j + dy[x]
        if nx>=0 and nx<r and ny>=0 and ny<c and home[nx][ny] != -1:
            count += 1
            tmp_home[nx][ny] += num
    home[i][j] -= (num*count)

#queue = deque()

def aircleaner():
    topr, topc = robot_loc[0]
    bottomr, bottomc = robot_loc[1]

    #위쪽 옮기기
    #tmp 써서 1칸씩 옮기는 것도 괜찮음.
    #bottom
    tmp = 0
    for i in range(topc+1, c):
        tmp, home[topr][i] = home[topr][i], tmp
        
    #right
    for i in range(topr-1, -1, -1):
        tmp, home[i][c-1] = home[i][c-1], tmp

    #top
    for i in range(c-2, -1,-1):
        tmp, home[0][i] = home[0][i], tmp

    #left
    for i in range(1,topr):
        tmp, home[i][0] = home[i][0], tmp


    #아래쪽
    #top
    tmp = 0
    for i in range(bottomc+1, c):
        tmp, home[bottomr][i] = home[bottomr][i], tmp
    
    #right
    for i in range(bottomr+1, r):
        #맨 끝쪽이 c-1임.
        tmp, home[i][c-1] = home[i][c-1], tmp
    
    #bottom
    for i in range(c-2,-1,-1):
        #r-1이 실질로 마지막 row
        tmp, home[r-1][i] = home[r-1][i], tmp
    
    #left
    for i in range(r-2,bottomr,-1):
        tmp, home[i][0] = home[i][0], tmp



while time:
    #미세먼지 확산
    #reset tmp_home
    tmp_home = [[0]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if home[i][j] > 0:
                #spread
                calculatevirus(i,j)
            elif home[i][j] == -1:
                robot_loc.append((i,j))

    for i in range(r):
        for j in range(c):
            #최종 바이러스 크기를 위해 더해주기 + tmp_home도 넣어주고 +2 해줘야 함.
            #amount += home[i][j]
            if tmp_home[i][j] > 0:
                home[i][j] += tmp_home[i][j]
                #amount += tmp_home[i][j]
                amount += home[i][j]
            
    #바람 불기
    #공기청정기가 방 중간에 있을때도 고려해야 하나?
    # for row in home:
    #     print(row)
    aircleaner()
    time -= 1

# for i in range(r):
#     print(home[i])
print(amount+2)
