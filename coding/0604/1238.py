# import sys
# input = sys.stdin.readline

# N, M, X = map(int, input().split())
# adjacency_list = {}

# for _ in range(M):
#     a, b, time = map(int, input().split())
#     if a in adjacency_list.keys():
#         adjacency_list[a].append((b, time))
#     else:
#         adjacency_list[a] = [(b, time)]

import heapq
def dijkstra(s):
    distance = [float('inf')] * (N + 1)
    distance[s] = 0
    q = []
    heapq.heappush(q, (0, s))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] >= dist:
            for v, val in homes[now]:
                if dist + val < distance[v]:
                    distance[v] = dist + val
                    heapq.heappush(q, (dist + val, v))
    return distance

N, M, X = map(int, input().split())
homes = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, time = map(int, input().split())
    homes[a].append([b, time])

answer = dijkstra(X) # X에서 모든 목적지까지의 거리 구하기
answer[0] = 0
for i in range(1, N+1):
    if i != X:
        result = dijkstra(i) # 모든 목적지에서 X까지의 거리 구하기 
        answer[i] += result[X]

print(max(answer))