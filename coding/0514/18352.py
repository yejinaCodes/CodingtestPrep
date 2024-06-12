import sys
import heapq
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
INF = int(1e9)

graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append((b, 1))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        #distance list에는 해당 node까지 최단거리를 저장하는 것임
        if distance[now] < dist:
            continue
        #now완 연결된 노드 확인하고 필요시 distance update하기
        for j in graph[now]:
            cost = dist + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                heapq.heappush(q, (cost, j[0]))

dijkstra(X)
answer = []
# X로부터 출발하여 도달할 수 있는 도시 중에서 최단 거리가 K인 모든 도시의 번호를 출력해야 함
for i in range(1, N+1):
    if distance[i] == K:
        answer.append(i)
if len(answer) == 0:
    print(-1)
else:
    for i in answer:
        print(i, end='\n')

# #adjacency list
# cities = {}
# visited = [False for _ in range(N)]
# for _ in range(M):
#     a, b = map(int, input().split())
#     if a not in cities.keys():
#         cities[a] = [b]
#     else:
#         cities[a].append(b)

