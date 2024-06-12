#10초 초과땜에 더 빨리 풀어야 함.
def solution(land):
    answer = 0
    n = len(land)
    m = len(land[0])

    check = 2
    oil_list = {}
    dx = [0,0,-1,1] #좌우위아래
    dy = [-1,1,0,0]
    def bfs(i,j):
        c = 1
        land[i][j] = check
        q = []
        q.append((i,j))
        while(q):
            x,y = q.pop(0)
            #land[x][y] = check
            for i in range(4):
                nx = dx[i] + x
                ny = dy[i] + y
                if nx>=0 and nx<n and ny>=0 and ny<m and land[nx][ny]==1:
                    c+= 1
                    q.append((nx,ny))
                    #land[nx][ny] = check
        return c
    #grouping    
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1:
                #bfs(i,j)
                oil_list[check] = (bfs(i,j))
                check += 1
    
    final = []
    answer = 0
    #제일 많은 석유양 뽑기
    for i in range(m):
        vertical = 0
        for j in range(n):
            if land[j][i] in final:
                continue
            elif (land[j][i]!= 0) and (land[j][i] in oil_list.keys()):
                final.append(land[j][i])
                vertical += oil_list[land[j][i]]
        answer = max(answer, vertical)
            
            
            #두번 계산하지 않도록 해줘야 함.
#             if land[j][i] in final:
#                 continue
#             elif land[j][i] != 0:
#                 for key,value in oil_list.items():
#                     if key == land[i][j]:
#                         vertical += value
                        
#         answer = max(answer, vertical)
    
    return answer

#dfs + backtracking 해야 하는 것 같음.

# def bfs(x,y):
#     dx = [0,0,-1,1]
#     dy = [-1,1,0,0]
    
    # if maze[x][y] == 1:
    #     #빨강일때 파랑이랑 겹치면 안됨
    #     current_not = 2
    # elif maze[x][y] == 2:
    #     #파랑일때 빨강이랑 겹치면 안됨
    #     current_not= 1
        
    #count도 해줘서 최단거리 계산해야함
#     while(queue_red or queue_blue)
#         redx, redy = queue_red.pop()
#         bluex, bluey = queue_blue.pop()
        
#         #for red
#         for i in range(4):
#             nx = dx[i] + x
#             ny = dy[i] + y
#             if nx>=0 and nx<n and ny>=0 and ny<m and maze[nx][ny] != 5
#             and maze[nx][ny] != current_not:
#                 #그럼 움직여도 됨.
#                 queue_red.append((nx,ny))
#             elif nx>=0 and nx<n and ny>=0 and ny<m and maze[nx][ny] != 5
#             and maze[nx][ny] != current_not: 

        
def solution(maze):
    answer = 0
    
    n = len(maze)
    m = len(maze[0])
    
    visited_red = [[0]*m for i in range(n)]
    visited_blue = [[0]*m for i in range(n)]
    answer = 10e9
    
    lastrx, lastry = 0
    lastbx, lastby = 0
    
    #빨간색과 파랑색으로 위치
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 1:
                redx, redy = i,j
                # red_position.append((i,j))
            elif maze[i][j] == 2:
                bluex, bluey = i,j
                # blue_position.append((i,j))
            elif maze[i][j] == 3:
                lastrx, lastry = i,j
            elif maze[i][j] == 4:
                lastbx, lastby = i,j
        
    #dfs for red and black if cannot then backtrack
    
    answer = 10e9
    #count하는거랑
    #최단거리를 구하는게 헷갈림..
    count = 0
    while true:
        if redx, redy == lastrx, lastry and bluex,bluey == lastbx, lastby:
            return answer
        if dfs_red(redx, redy):
            if dfs_blue(bluex,bluey):
                #count += 1
                
            


# def dfs_red(x,y):
#     dx = [0,0,-1,1]
#     dy = [-1,1,0,0]
#     if x,y == lastrx, lastry:
#         return true
#     for i in range(4):
#         nx = dx[i] + x
#         ny = dy[i] + y
#         if nx>=0 and nx<n and ny>=0 and ny<m and maze[nx][ny] != 5
#         and nx, ny!= bluex, bluey  and visited_red[nx][ny]==0:
#             maze[nx][ny] = 1
#             visited_red[nx][ny] = 1
#             redx, redy = nx, ny
#             return true
#         # elif maze[nx][ny] == 3 or maze[nx][ny] == 1:
#         #     maze[nx][ny] = 1
#         #     visited_red[nx][ny] = 1
#         #     redx, redy = nx, ny
#         #     return true
        
#     return false
#             #dfs(nx, ny)
        
# def dfs_blue(x,y):
#     dx = [0,0,-1,1]
#     dy = [-1,1,0,0]
#     if x,y == lastbx, lastby:
#         return true
#     for i in range(4):
#         nx = dx[i] + x
#         ny = dy[i] + y
#         if nx>=0 and nx<n and ny>=0 and ny<m and maze[nx][ny] != 5
#         and nx, ny!= redx, redy  and visited_blue[nx][ny] == 0:
#             maze[nx][ny] = 2
#             visited_blue[nx][ny] = 1
#             bluex, bluey = nx, ny
#             return true
#         elif maze[nx][ny] == 4 or maze[nx][ny] == 2:
#             maze[nx][ny] = 2
#             visited_red[nx][ny] = 1
#             bluex, bluey = nx, ny
#             return true
#     return false
#             #dfs(nx, ny)
    
#         #파란색도 경우의 수가 많고.
#         #빨간색도 경우의 수가 많다.
        
#         #2개에 대해서 dfs backtracking?


    
#     return answer
                

