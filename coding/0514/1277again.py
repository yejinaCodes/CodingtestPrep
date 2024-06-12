from math import sqrt
import heapq

N, W = map(int, input().split())
M = float(input())

vertex = []
for _ in range(N):
    vertex.append(list(map(int, input().split())))

def distance(x1, y1, x2, y2):
    return sqrt((x2-x1)**2 + (y2-y1)**2)

# adjacency graph 초기화
graph = [[1e9] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        graph[i][j] = distance(vertex[i][0], vertex[i][1], vertex[j][0], vertex[j][1])
        # M보다 거리가 멀 경우
        if graph[i][j] > M:
            graph[i][j] = 1e9

# 이미 연결된 전선은 0으로 세팅
for _ in range(W):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 0
    graph[b-1][a-1] = 0

# dijkstra
# 해당 index node까지 최단 거리 기록
distance = [1e9] * N
distance[0] = 0

q = []
heapq.heappush(q, (0, 0)) # 해당 node까지의 거리, 해당 노드 index

while q: # 결국 q에는 최단 path를 하나 찾게 될 것임.
    dist, node = heapq.heappop(q)
    
    # 이미 방문해서 최단 값을 구했을 경우
    if distance[node] < dist:
        continue

    # 해당 노드와 다른 모든 노드에 대해 진행
    for i, cost in enumerate(graph[node]):
        if cost == 1e9: # M보다 큰 거리면 방문 못함. 혹은 i==j일 경우
            continue
        newCost = dist + cost
        if newCost < distance[i]:
            distance[i] = newCost
            heapq.heappush(q, (newCost, i))

print(int(distance[N-1] * 1000))