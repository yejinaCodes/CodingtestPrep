import sys
from collections import deque
import heapq
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

#input taxi location
taxi_x, taxi_y = map(int,input().split())
customers_data = []

#input customer location and destination
for i in range(M):
    tmp = list(map(int,input().split()))
    customers_data.append(tmp)

customers_data = sorted(customers_data, key = lambda x:(x[0], x[1]))

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(tmp, visited, destinx, destiny, distance):
    q = deque()
    q.append((destinx, destiny, distance))
    visited[destinx][destiny] = True
    while q:
        x, y, d = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0<nx<=N and 0<ny<=N and map_[nx][ny] == 0 and visited[nx][ny] == False:
                q.append((nx, ny, d+1))
                tmp[nx][ny] = d+1
                visited[nx][ny] = True
    return tmp

while customers_data:
    #heapq를 tuple로 사용하기
    nearest = []
    #taxi와 제일 가까운 customer 테우기
    #bfs 한번만 돌리게 해야 한다. tmp에 taxi기준으로 거리 미리 계산해놓고 customer위치에 해당 위치까지의 거리가
    #저장되어 있음.
    visited = [[False]*(N+1) for _ in range(N+1)]
    tmp = [[-1]*(N+1) for _ in range(N+1)]
    tmp[taxi_x][taxi_y] = 0

    tmp = bfs(tmp, visited,taxi_x, taxi_y, 0)
    for i in range(len(customers_data)):
        startx, starty, destinx, destiny = customers_data[i]
        heapq.heappush(nearest, (tmp[startx][starty], i))

    closest_dis, closest_customer_idx = heapq.heappop(nearest)
    if closest_dis == -1:
        print(-1)
        sys.exit()

    if fuel-closest_dis <= 0:
        print(-1)
        sys.exit()

    fuel-= closest_dis

    #최단거리로 customer을 목적지로 옮기기
    sx,sy,ddx,ddy = customers_data[closest_customer_idx]
    visited = [[False]*(N+1) for _ in range(N+1)]
    tmp = [[-1]*(N+1) for _ in range(N+1)]
    #tmp에 customer위치에서 destination까지의 거리 값 구하기
    tmp = bfs(tmp, visited, sx, sy, 0)
    destination = tmp[ddx][ddy]

    #마지막으로 값이 0이여도 되기 때문에 <= 를 쓰면 안됨.
    if fuel - destination < 0:
        print(-1)
        sys.exit()

    fuel -= destination

    #taxi 자리 옮겨주기 + 이동한 customer빼주기
    taxi_x, taxi_y = ddx, ddy
    customers_data.pop(closest_customer_idx)

    #fuel 빼주고 이동거리*2 채워주기
    fuel += destination*2

print(fuel)