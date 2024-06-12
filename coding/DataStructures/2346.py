import sys
from collections import deque

sys.stdin = open('./popballoon.txt')
n = int(input())
balloons = list(map(int,input().split()))

queue = deque()
for i in range(n):
    queue.append((i+1, balloons[i]))

#넣을때 (값, 인텍스 형태로 넣기)
#인텍스 안쓰면 느려서 에러뜸
result = [] #퐁선 안에 있는 index 값들이 들어있음.

index, find = queue.popleft()
result.append(index)

while queue:
    if find > 0:
        for i in range(find-1):
            index, x = queue.popleft()
            queue.append((index,x))

        index, find = queue.popleft()
        result.append(index)

    elif find < 0:
        for i in range(abs(find)-1):
            index, x = queue.pop()
            queue.appendleft((index,x))
    
        index, find = queue.pop()
        result.append(index)
for i in result:
    print(i, end=' ')


# result.append(balloons.index(x)+1)

# while queue:
#     find = x
#     #print(find)
#     if find > 0:
#         #풍선들이 왼쪽으로 움직여야 함
#         for i in range(find-1):
#             y = queue.popleft()
#             #print(y)
#             queue.append(y)
#     else: #풍선들이 오른쪽으로 움직여야 함
#         for i in range(abs(find)):
#             y = queue.pop()
#             queue.appendleft(y)
#     x = queue.popleft()
#     result.append(balloons.index(x)+1)
    

# for i in range(len(result)):
#     print(result[i], end=' ')