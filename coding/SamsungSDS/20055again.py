import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
conveyor_belt = deque(map(int, input().split()))
robots = deque(False for _ in range(N))
results = 0

while True:
    #1. 한 칸 회전
    conveyor_belt.rotate(1)
    robots.rotate(1)
    
    #2. 로봇 이동
    if robots[-1] == True:
        robots[-1] = False
    for i in range(N-2, -1, -1):
        if robots[i] == True:
            if conveyor_belt[i+1] > 0 and robots[i+1] == False:
                robots[i] = False
                robots[i+1] = True
                conveyor_belt[i+1] -= 1
        #이 부분이 중요!!
        #이동 후 내려가는 위치에 로봇이 존재할 경우가 존재하기 때문에 다시 한번 False로 로봇을 없애줘야 함.
        robots[-1] = False

    #3. 로봇 올리기
    if conveyor_belt[0] > 0 and robots[0] == False:
        conveyor_belt[0] -= 1
        robots[0] = True

    results += 1
    #4. 내구도 확인
    if conveyor_belt.count(0) >= K:
        print(results)
        break

