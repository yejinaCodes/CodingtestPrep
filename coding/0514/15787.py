import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
orders = []
for _ in range(M):
    orders.append(list(map(int, input().split())))

entire_train = [deque(0 for _ in range(20)) for _ in range(N)]

for order in orders:
    if order[0] == 1:
        if entire_train[order[1]-1][order[2]-1] == 0:
            entire_train[order[1]-1][order[2]-1] = 1
    elif order[0] == 2:
        if entire_train[order[1]-1][order[2]-1] == 1:
            entire_train[order[1]-1][order[2]-1] = 0
    elif order[0] == 3:
        entire_train[order[1]-1].rotate(1)
        entire_train[order[1]-1][0] = 0
    elif order[0] == 4:
        entire_train[order[1]-1].rotate(-1)
        entire_train[order[1]-1][-1] = 0

#은하수 건넌 train count하기 위해서는 set 사용하기
milky_way = []
for i in range(N):
    if list(entire_train[i]) not in milky_way:
        milky_way.append(list(entire_train[i]))

print(len(milky_way))
# N <= 100000 이여서 for loop하면 시간초과 뜰 줄 알았음