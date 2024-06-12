from collections import deque
import sys

input = sys.stdin.readline

first = list(map(str, input().split()))
second = list(map(str, input().split()))
third = list(map(str, input().split()))
fourth = list(map(str, input().split()))

entire_wheel = []
first = deque(map(int,str(first[0])))
second = deque(map(int,str(second[0])))
third = deque(map(int,str(third[0])))
fourth = deque(map(int,str(fourth[0])))

entire_wheel.append(first)
entire_wheel.append(second)
entire_wheel.append(third)
entire_wheel.append(fourth)

times = int(input())
rotate_sequence = []
for time in range(times):
    rotate_wheel, d = map(int, input().split())
    rotate_sequence.append((rotate_wheel-1, d))

#돌릴 wheel 지정하고
#양쪽 check하고 tmp 리스트에 넣어주고
#방향에 맞게 돌려주기
#k번 이후 점수 합산하기
result = 0

for time in range(times):
    wheel, direction = rotate_sequence[time]

    tmpleft = deque()
    tmpleft.append((wheel, direction))
    tmpright = deque()
    tmpright.append((wheel, direction))
    while True:
        current = 0
        #left check
        for i in range(wheel-1, -1, -1):
            if entire_wheel[tmpleft[current][0]][6] != entire_wheel[i][2]:
                tmpleft.appendleft((i, tmpleft[current][1]*-1))
            else:
                break
        #right check
        for j in range(wheel+1, 4):
            if entire_wheel[tmpright[current][0]][2] != entire_wheel[j][6]:
                tmpright.appendleft((j, tmpright[current][1]*-1))
            else:
                break
        break

    tmpright.pop()
    #print('left', tmpleft)
    #print('right', tmpright)
    for i in range(len(tmpleft)):
        #시계방향일 경우
        w, dir = tmpleft[i]
        if dir == 1:
            t = entire_wheel[w].pop()
            entire_wheel[w].appendleft(t)
        #반시계방향일 경우
        elif dir == -1:
            t = entire_wheel[w].popleft()
            entire_wheel[w].append(t)
    for j in range(len(tmpright)):
        #시계방향일 경우
        w, dir = tmpright[j]
        if dir == 1:
            t = entire_wheel[w].pop()
            entire_wheel[w].appendleft(t)
        #반시계방향일 경우
        elif dir == -1:
            t = entire_wheel[w].popleft()
            entire_wheel[w].append(t)


for t in range(4):
    if t == 0:
        if entire_wheel[t][0] == 1:
            result += 1
    elif t == 1:
        if entire_wheel[t][0] == 1:
            result += 2
    elif t == 2:
        if entire_wheel[t][0] == 1:
            result += 4
    elif t == 3:
        if entire_wheel[t][0] == 1:
            result += 8

print(result)