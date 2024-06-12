def solution(maze):
    answer = [1e9]
    
    n = len(maze)
    m = len(maze[0])
    
    visited_red = [[0]*m for i in range(n)]
    visited_blue = [[0]*m for i in range(n)]
    
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 1:
                (redx, redy) = (i,j)
            elif maze[i][j] == 2:
                (bluex, bluey) = (i,j)
                
    visited_red[redx][redy] = 1
    visited_blue[bluex][bluey] = 1
    
    def backtracking(redx, redy, bluex, bluey, count):
        dx = [0,0,-1,1]
        dy = [-1,1,0,0]
        
        if maze[redx][redy] == 3 and maze[bluex][bluey] == 4:
            answer[0] = min(answer[0], count)
            return 
        
        if count >= answer[0]:
            return
        
        for i in range(4):
            rednx = dx[i] + redx
            redny = dy[i] + redy
            
            if maze[redx][redy] == 3:
                rednx = redx
                redny = redy
            else:
                if rednx<0 or rednx>=n or redny<0 or redny>=m:
                    continue
                if visited_red[rednx][redny] == 1:
                    continue
                if maze[rednx][redny] == 5:
                    continue
            
            for j in range(4):
                bluenx = dx[j] + bluex
                blueny = dy[j] + bluey
                
                if maze[bluex][bluey] == 4:
                    bluenx = bluex
                    blueny = bluey
                    
                else:
                    if bluenx<0 or bluenx>=n or blueny<0 or blueny>=m:
                        continue
                    if visited_blue[bluenx][blueny] == 1:
                        continue
                    if maze[bluenx][blueny] == 5:
                        continue
            
                if bluenx == redx and blueny == redy and rednx == bluex and redny == bluey:
                    continue
                if rednx == bluenx and redny == blueny:
                    continue
                
                #가지치기를 다 통과했을 경우
                visited_red[rednx][redny] = 1
                visited_blue[bluenx][blueny] = 1
                
                backtracking(rednx, redny, bluenx, blueny, count+1)
                
                #가지치기 당했으면 back
                visited_red[rednx][redny] = 0
                visited_blue[bluenx][blueny] = 0
    
    backtracking(redx, redy, bluex, bluey, 0)
    
    if answer[0] == 1e9:
        answer[0] = 0

    return answer[0]