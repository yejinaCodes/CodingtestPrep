
n = int(input())
result = [[0] * n for _ in range(n)]
students = [list(map(int, input().split())) for _ in range(n**2)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for student in students:
    available = []

    for i in range(n):
        for j in range(n):

            #빈자리 존재
            if result[i][j] == 0:
                prefer, empty = 0, 0

                #4방향 확인
                for d in range(4):
                    nx = dx[d] + i
                    ny = dy[d] + j

                    if 0 <= nx < n and 0 <= ny < n:
                        if result[nx][ny] in student[1:]:
                            prefer += 1
                        
                        if result[nx][ny] == 0:
                            empty += 1

                available.append((i, j, prefer, empty))
    available.sort(key = lambda x: (-x[2], -x[3], x[0], x[1]))
    result[available[0][0]][available[0][1]] = student[0]

answer = 0
score = [0, 1, 10, 100, 1000]
students.sort()

for i in range(n):
    for j in range(n):
        count = 0

        for d in range(4):
            nx = dx[d] + i
            ny = dy[d] + j

            if 0 <= nx < n and 0 <= ny < n:
                if result[nx][ny] in students[result[i][j] - 1]:
                    count += 1
        answer += score[count]
    
print(answer)