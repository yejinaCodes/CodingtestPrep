#simulation 문제

import sys
from collections import deque

input = sys.stdin.readline

trucks_num, bridge_length, bridge_weight = map(int,input().split())
trucks = deque(list(map(int,input().split())))

#bridge 길이만큼 position 만들기
bridge = [0] * bridge_length

time = 0
while bridge:
    bridge.pop(0)
    #들어간 모든 트럭이 pop될때까지 time을 카운트해줘야 함. 그래서 여기 있어야 함.
    time+=1
    #trucks리스트에 값이 존재할 경우:
    if trucks:
        if sum(bridge) + trucks[0] <= bridge_weight:
            bridge.append(trucks.popleft())

        else:
            bridge.append(0)

print(time)