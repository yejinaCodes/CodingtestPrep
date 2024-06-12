#bfs로 풀어보기로 함
n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(map(int,input())))
dx = [1,-1,0,0]
dy = [0,0,1,-1] 
result =[]

def bfs(matrix, startx, starty):
    queue = [(startx,starty)]
    check = 0
    if matrix[startx][starty] == 1:
        check+= 1
        matrix[startx][starty] = 0
    
    while queue:
        startx,starty = queue.pop(0)
        for i in range(4):
            x = startx + dx[i]
            y = starty + dy[i]
            if x < n and x >= 0 and y < n and y >= 0 and matrix[x][y] == 1:
                queue.append((x, y))
                matrix[x][y] = 0
                check += 1
    result.append(check)

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            bfs(matrix, i,j)

print(len(result))
result.sort()
for i in result:
    print(result[i])

            