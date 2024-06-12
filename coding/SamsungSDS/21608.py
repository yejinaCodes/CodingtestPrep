import sys
input = sys.stdin.readline

N = int(input())
students = []
for i in range(N**2):
    tmp = list(map(int, input().split()))
    students.append(tmp)

result = [[0] * N for _ in range(N)]
satisfaction = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for student in students:
    candidates = []
    #학생 자리 정하기
    for i in range(N):
        for j in range(N):
            empty = 0
            likes = 0
            if result[i][j] == 0:
                for d in range(4):
                    nx = dx[d] + i
                    ny = dy[d] + j
                    if 0 <= nx < N and 0 <= ny < N:
                        if result[nx][ny] == 0:
                            empty += 1
                        elif result[nx][ny] in student[1:]:
                            likes += 1
                candidates.append((i, j, likes, empty))
    candidates.sort(key = lambda x:(-x[2], -x[3], x[1], x[2]))
    result[candidates[0][0]][candidates[0][1]] = student[0]

scores = [0, 1, 10, 100, 1000]
students.sort()

#만족도 구하기
for i in range(N):
    for j in range(N):
        num = result[i][j]
        tmp = 0
        for d in range(4):
            nx = dx[d] + i
            ny = dy[d] + j
            if 0 <= nx < N and 0 <= ny < N:
                if result[nx][ny] in students[num - 1]:
                    tmp += 1
        satisfaction += scores[tmp]
    
print(satisfaction)