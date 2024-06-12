import sys
from collections import deque

input = sys.stdin.readline

n,m,rotation = map(int,input().split())

matrix = []
for i in range(n):
    matrix.append(list(map(int,input().split())))

result = [[0]*m for i in range(n)]
#rotation 완료했다면 종료하기 위함.
#donematrix = [[False]*m for i in range(n)]
#print(donematrix)


rotation_queue = deque()
#몇번 돌릴지 생각해야 함.

#만약에 5x3일 경우
#일렬 값에 대해서 rotation이 필요없다?!

#1차원 deque로 변환한 다음에 rotate하기 
loops = min(n,m)//2
for i in range(loops):

    rotation_queue.clear()
    #matrix[i][i:m-i] 범위를 이렇게 접근할 수 있음. 상단 부분에 해당
    rotation_queue.extend(matrix[i][i:m-i])
    #오르쪽 위에서 아래 방향으로
    rotation_queue.extend([row[m-i-1] for row in matrix[i+1:n-i-1]])
    #반대 방향으로 extend해줘야 함.
    rotation_queue.extend(matrix[n-i-1][i:m-i][::-1])
    #왼쪽 부분. 아래서 위로 extend해줘야 함.
    rotation_queue.extend([row[i]for row in matrix[i+1:n-i-1]][::-1])

    #rotate이라는 함수가 이미 존재함...
    rotation_queue.rotate(-rotation)


    #다시 2차원으로 바꿔주기
    for x in range(i, m-i):
        result[i][x] = rotation_queue.popleft()
    for x in range(i+1, n-i-1):
        result[x][m-i-1] = rotation_queue.popleft()
    for x in range(m-i-1, i-1,-1):
        #print(x)
        result[n-i-1][x] = rotation_queue.popleft()
    for x in range(n-i-2, i,-1):
        result[x][i] = rotation_queue.popleft()

for i in result:
    i= str(i).strip('[]')
    print(i.replace(',',''))


# def rotate(x,y):
    






# def rotate(x,y):

#     progress = deque()
#     tmp = matrix[x][y]

#     if (x+1)< n and donematrix[x+1][y] == 0 and matrix[x+1][y] !=0:
#         progress.append(matrix[x][y])
#         matrix[x+rotation][y] = tmp
    
    
#     elif (x+rotation)











# for i in range(rotation):




# #     tmp = matrix[]