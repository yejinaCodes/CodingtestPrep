#집중국의 수신 가능 영역은 고속도로 상에서 연결된 구간으로 나타나게 된다.

#각 집중국의 수신 가능영역의 거리의 합의 최솟값을 구해야 함.
#1번 예시에서 2개 그룹으로 나눈다고 생각했을 때 각 그룹에 하나의 집중국이 있다고 생각하면 됨?
#[1,3,6,6,7,9] 에서 1,3사이에 1개의 집중국, 그리고 6,6,7,9사이에 1개의 집중국.
#즉, 1과3사이에 집중국 한개를 세우면 1과는 1의 거리를, 3과는 2의 거리를 가지게 된다. 혹은 함이 3-1= 2의 거리이다.


#중요한접: 합이 최솟값이여함.


import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
sensors = list(map(int,input().split()))

#k가 크거나 같으면 0. 같다고만 쓰면 런타임 에러뜸
if k>=n:
    print(0)
    sys.exit(0)

sensors.sort()
distance = []

for i in range(1, n):
    distance.append(sensors[i]-sensors[i-1])

distance.sort(reverse=True)
#print(distance)

for i in range(k-1):
    distance.pop(0)
print(sum(distance))
