def solution(maze):
    row, col = len(maze), len(maze[0])
    answer = [1e99]
    
    move = [(1,0), (-1,0), (0,1), (0,-1)]
    
    red_visited = [[False] * col for _ in range(row)]
    blue_visited = [[False] * col for _ in range(row)]
    
    for r in range(row):
        for c in range(col):
            if maze[r][c] == 1:
                red = (r, c)
            elif maze[r][c] == 2:
                blue = (r, c)
    
    red_visited[red[0]][red[1]] = True
    blue_visited[blue[0]][blue[1]] = True
    
    def backtracking(red_loc, blue_loc, m):
        if maze[red_loc[0]][red_loc[1]] == 3 and maze[blue_loc[0]][blue_loc[1]] == 4:
            answer[0] = min(answer[0], m)
            return
        
        if answer[0] <= m:
            return
        
        for i in range(4):
            red_nr = red_loc[0] + move[i][0]
            red_nc = red_loc[1] + move[i][1]
            
            if maze[red_loc[0]][red_loc[1]] == 3:
                red_nr = red_loc[0]
                red_nc = red_loc[1]
            else:
                if red_nr < 0 or red_nr >= row or red_nc < 0 or red_nc >= col: continue
                if red_visited[red_nr][red_nc]: continue
                if maze[red_nr][red_nc] == 5: continue
            
            
            for j in range(4):
                blue_nr = blue_loc[0] + move[j][0]
                blue_nc = blue_loc[1] + move[j][1]
                
                if maze[blue_loc[0]][blue_loc[1]] == 4:
                    blue_nr = blue_loc[0]
                    blue_nc = blue_loc[1]
                else:
                    if blue_nr < 0 or blue_nr >= row or blue_nc < 0 or blue_nc >= col: continue
                    if blue_visited[blue_nr][blue_nc]: continue
                    if maze[blue_nr][blue_nc] == 5: continue
                
                
                if red_loc[0] == blue_nr and red_loc[1] == blue_nc and blue_loc[0] == red_nr and blue_loc[1] == red_nc: continue
                if red_nr == blue_nr and red_nc == blue_nc: continue
                
                new_red = (red_nr, red_nc)
                new_blue = (blue_nr, blue_nc)
                
                red_visited[red_nr][red_nc] = True
                blue_visited[blue_nr][blue_nc] = True
                
                backtracking(new_red, new_blue, m+1)
                
                blue_visited[blue_nr][blue_nc] = False
                red_visited[red_nr][red_nc] = False
                
                
    backtracking(red, blue, 0)
    if answer[0] == 1e99:
        answer[0] = 0
    
    return answer[0]