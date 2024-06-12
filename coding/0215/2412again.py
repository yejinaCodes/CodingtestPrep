import sys
from collections import deque
input = sys.stdin.readline

n, T = map(int,input().split())
#list말고 set을 사용해야 함.
homes = set()
#homes = []

for i in range(n):
    a,b = map(int,input().split())
    homes.add((a,b))

# #오름차순으로 배열하기
# homes.sort()
#count = 0
#bfs로 최소 이동 횟수 찾기
queue = deque()
#값이 3개 이기때문에 list으로 넣어준다.
queue.append((0,0,0))
flag = False

while queue:
    x,y, count = queue.popleft()
    if y == T:
        flag = True
        break
    #움직일 수 있는 범위 내에 있는 값들에 대해서만 search하고 queue에 append한다.
    #그래서 set을 사용해야 한다. 0(1)으로 search 가능하기 때문
    for i in range(-2, 3):
        for j in range(-2,3):
            nx = x + i
            ny = y + j
            if (nx,ny) in homes:
                queue.append((nx,ny, count+1))
                homes.remove((nx,ny))
if flag:
    print(count)
else:
    print(-1)    


# def bfs(i,j):
#     global count
#     queue = []
#     queue.append((i,j))
#     while queue:
#         x,y= queue.pop()

#         if y == T:
#             flag = True
#             break

#         for i in range(n):
#             if abs(homes[i][0]-x) <=2 and abs(homes[i][1]-y) <=2:
#                 queue.append(homes[i])
#                 homes.remove(homes[i])


# if flag:
#     print(count)
# else:
#     print(-1)




# bfs(0,0)
# print(count)
