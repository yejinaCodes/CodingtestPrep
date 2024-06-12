import sys
from collections import deque
input = sys.stdin.readline

#input 데이터 받기
N,M,fuel = map(int,input().split())
map_ = []

for i in range(N):
    tmp = list(map(int,input().split()))
    map_.append(tmp)

taxi_x, taxi_y = map(int,input().split())

customers_data = []

for i in range(M):
    tmp = list(map(int,input().split()))
    customers_data.append(tmp)

#미리 행, 렬 작은 순으로 정리해놓기
customers_data = sorted(customers_data, key = lambda x:(x[0],x[1]))
#print(customers_data)

dx = [-1,0,1,0] #시계방향
dy = [0,1,0,-1]

def bfs(startx,starty,distance):
    global taxi_x, taxi_y
    q = deque()
    q.append((startx,starty,distance))
    #print(q)
    while q:
        x, y, distance = q.popleft()
        #여기로 못들어가는 것 같음..why?
        if (x,y) == (taxi_x, taxi_y):
            return distance
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            #print(nx,ny)
            if 0<=nx<N  and 0<=ny<N and map_[nx][ny] == 0:
                #print(nx,ny)
                q.append((nx,ny,distance+1))

def fuel_calculation(fuel_used):
    global fuel
    fuel -= fuel_used

while customers_data:
    #모든 customer과의 최단거리 구하기
    nearest = {}
    #print('check')
    for i in range(len(customers_data)):
        startx, starty, destinx, destiny = customers_data[i]
        nearest[i] = bfs(startx, starty,0)
        #print('cc')
    #제일 작은 값의 index사용하기
    clos_cust = nearest.index(min(nearest.items()))
    #print(clos_cust)
    fuel_used = nearest[clos_cust]
    if fuel_calculation(fuel_used) < 0:
        print(-1)
        sys.exit()
    #도착지까지 이동
    to_dest = bfs(customers_data[clos_cust][2],customers_data[clos_cust][3],0)

    if fuel_calculation(to_dest) < 0:
        print(-1)
        sys.exit()
    else:
        #2배 연료 충전
        fuel += to_dest*2
        taxi_x, taxi_y = customers_data[clos_cust][2], customers_data[clos_cust][3]
        customers_data.pop(clos_cust)

print(fuel)