import sys
from collections import deque

input = sys.stdin.readline
r,c = map(int,input().split())

matrix = []
heaven = []
visited = [([0]*r) for i in range(c)]
water = deque()
beaver = deque()
empty_spaces = 0

for i in range(r):
    check = str(input().strip())
    matrix.append(check)
    for j in range(c):
        if check[j] == 'D':
            heaven.append((i,j))
        elif check[j] == '*':
            water.append((i,j))
        elif check[j] == 'S':
            beaver.append((i,j))
        elif check[j] == '.':
            empty_spaces += 1

dx = [0,0,-1,1] #우좌위아래
dy = [1,-1,0,0]

#print(empty_spaces)
#물이 고슴도치 위치에 올 경우?

def watering(water):
    global empty_spaces
    for i in range(len(water)):
        x,y = water.popleft()
        # print(matrix[x][y])
        visited[x][y] = 1
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if nx>=0 and nx<r and ny>=0 and ny<r and visited[nx][ny] == 0:
                water.append((nx,ny))
                #empty_spaces -= 1
                
                visited[nx][ny] = 1        

def beavermove(beaver):
    global empty_spaces
    #check = 0
    positionx,positiony = beaver.pop()
    if (positionx,positiony)in heaven:
        return True
    for i in range(4):
        nx = dx[i] + positionx
        ny = dx[i] + positiony
        if nx>=0 and nx<r and ny>=0 and ny<r and visited[nx][ny] == 0:
            print((nx,ny))
            beaver.append((nx,ny))
            #check += 1
    return False

def bfs():
    count =0
    global empty_spaces
    while beaver:
        # if empty_spaces < 1:
        #     print('KAKTUS')
        #     sys.exit()
        watering(water)
        count += 1
        if beavermove(beaver):
            print (count)
            sys.exit()
    print('KAKTUS')
    sys.exit()
    

bfs()

# def bfs():
#     queue = []
#     global empty_spaces
#     count = 0
#     while empty_spaces > 0:
#         watering(water)
#         count += 1
#         if beavermove(beaver):
#             print (count)
#     answer = 'KAKTUS'
#     return (answer)


# def bfs(startnode):
#     queue = [startnode]
#     visited[startnode] = 0

#     while queue:
#         startnode = queue.pop(0)
#         bfs_result.append(startnode)
#         for i in range(1, n+1):
#             if visited[i] == 1 and matrix[startnode][i] == 1:
#                 queue.append(i)
#                 visited[i] = 0

        
        
        
        
        
        
        