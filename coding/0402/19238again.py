import sys
from collections import deque
import heapq
import time
input = sys.stdin.readline

N,M,fuel = map(int,input().split())
#행,열에 0 list 추가해주기
map_ = [[0] for i in range(N+1)]
for i in range(N):
    map_[0].append(0)

#input map
for i in range(1, N+1):
    tmp = list(map(int,input().split()))
    map_[i] += tmp

taxi_x, taxi_y = map(int,input().split())
customers_data = []

for i in range(M):
    tmp = list(map(int,input().split()))
    customers_data.append(tmp)

customers_data = sorted(customers_data, key = lambda x:(x[0], x[1]))

dx = [-1,0,1,0]
dy = [0,1,0,-1]

#taxi와 customer과의 최단거리 찾기 
def bfs(startx, starty,tx_dx, ty_dy, distance, visited):
    q = deque()
    q.append((startx, starty,distance))
    #start_time = time.process_time()
    while q:
        x,y,distance = q.popleft()
        if x == tx_dx and y == ty_dy:
            #end_time = time.process_time()
            #print(f"time in while elapsed : {int(round((end_time - start_time) * 1000))}ms")
            return distance
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0<nx<=N and 0<ny<=N and map_[nx][ny] == 0 and visited[nx][ny] == False:
                q.append((nx, ny, distance+1))
                visited[nx][ny] = True
    #end_time = time.process_time()
    #print(f"time 1 elapsed : {int(round((end_time - start_time) * 1000))}ms")
    return -1

#bfs 한번만 돌리게 해야 한다.
while customers_data:
    #heapq를 tuple로 사용하기
    nearest = []
    #taxi와 제일 가까운 customer 테우기

    for i in range(len(customers_data)):
        visited = [[False]*(N+1) for _ in range(N+1)]
        startx, starty, destinx, destiny = customers_data[i]
        tmp = bfs(startx, starty, taxi_x, taxi_y, 0, visited)
        if tmp < 0:
            print(-1)
            sys.exit()
        else:
            heapq.heappush(nearest, (tmp,i))

    closest_dis, closest_customer_idx = heapq.heappop(nearest)
    #closest_customer_idx = nearest.index(closest_cus)

    #customer을 태우러 가는 길에 fuel 바닥날 경우
    if fuel-closest_dis <= 0:
        print(-1)
        sys.exit()

    fuel-= closest_dis

    #최단거리로 customer을 목적지로 옮기기
    sx,sy,ddx,ddy = customers_data[closest_customer_idx]
    #print(sx,sy,ddx,ddy)
    visited = [[False]*(N+1) for _ in range(N+1)]

    #start_time = time.process_time()
    destination = bfs(sx,sy,ddx,ddy, 0, visited)

    #end_time = time.process_time()
    #print(f"time 2 elapsed : {int(round((end_time - start_time) * 1000))}ms")
    if fuel - destination <= 0:
        print(-1)
        sys.exit()

    fuel -= destination

    #taxi 자리 옮겨주기 + 이동한 customer빼주기
    taxi_x, taxi_y = ddx, ddy
    customers_data.pop(closest_customer_idx)

    #fuel 빼주고 이동거리*2 채워주기
    fuel += destination*2

print(fuel)