#stack에서 pop(0)을 쓰지 말고 queue로 popleft하면 더 좋음
#location을 list로 말고 hash map사용하면 더 좋은 것 같음.


#백준4396
import sys
sys.stdin = open("./0125/1_maze_input.txt", "r")
n = int(input())

location = []
flag = False
user_input = []
for i in range(n):
    pan = list(input())
    for p in range(n):
        if pan[p] == '*':
            location.append((i,p))

for x in range(n):
    answer = list(input())
    for a in range(n):
        if answer[a] == 'x':
            if (x,a) in location:
                user_input.append((x,a))
                flag = True
            else:
                user_input.append((x,a))

result = [[9] * n for i in range(n)]

#우,좌,상,하 + 시계방향 대각선
dx = [0,0,-1,1,-1,1,1,-1]
dy = [1,-1,0,0,1,1,-1,-1]

while user_input:
    check1,check2 = user_input.pop(0)
    check = 0
    #print(check1,check2)
    #숫자 계산. 방향 확인하기
    for i in range(8):
        nx = check1 + dx[i]
        ny = check2 + dy[i]
        if nx<n and nx>=0 and ny<n and ny>=0 and (nx,ny) in location:
            check += 1
    result[check1][check2] = check

if flag:
    for i in range(n):
        for j in range(n):
            if (i,j) in location:
                print('*', end = '')
            elif result[i][j] == 9:
                print('.', end = '')
            else:
                #print('.', end = '')
                print(result[i][j], end = '')
        print()
else:
    for i in range(n):
        for j in range(n):
            if result[i][j] == 9:
                print('.', end = '')
            else:
                print(result[i][j], end ='')
        #한 줄 띄우기
        print()



# #bad result print
# if flag == True:
#     while user_input:
#         check1,check2 = user_input.pop(0)
#         check = 0
#         #print(check1,check2)
#         #숫자 계산. 방향 확인하기
#         for i in range(8):
#             nx = check1 + dx[i]
#             ny = check2 + dy[i]
#             if nx<n and nx>=0 and ny<n and ny>=0 and (nx,ny) in location:
#                 check += 1

#         result[check1][check2] = check

# #good result print
# else:
#     while user_input:
#         check1,check2 = user_input.pop(0)
#         #print(check1, check2)
#         check = 0
#         #숫자 계산. 방향 확인하기
#         for i in range(8):
#             nx = check1 + dx[i]
#             ny = check2 + dy[i]
#             if nx<n and nx>= 0 and ny<n and ny>=0 and (nx,ny) in location:
#                 check += 1
#         result[check1][check2] = check
# for i in result:
#     print(i)
# #string이랑 int랑 같이 출력이 되나?
# if flag:
#     for i in range(n):
#         for j in range(n):
#             if (i,j) in location:
#                 print('*', end = '')
#             elif result[i][j] == 9:
#                 print('.', end = '')
#             else:
#                 #print('.', end = '')
#                 print(result[i][j], end = '')
#         print()

# else:
#     for i in range(n):
#         for j in range(n):
#             if result[i][j] == 9:
#                 print('.', end = '')
#             else:
#                 print(result[i][j], end ='')
#         #한 줄 띄우기
#         print()