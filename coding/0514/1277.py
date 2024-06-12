import heapq
import math

N, W = map(int, input().split())
M = float(input())
nodes_position = [[]]
for _ in range(N):
    nodes_position.append(list(map(int, input().split())))

#1에서 해당 노드까지의 최단 거리 list
distance = [1e9 for _ in range(N+1)]

def calculate(x, y):
    i, j = nodes_position[x]
    ii, jj = nodes_position[y]
    return math.sqrt(abs(i-ii)+ abs(j-jj))

adjacency_list = [[] for _ in range(N+1)]
#print(adjacency_list)
for _ in range(W):
    a, b = map(int, input().split())
    dist = calculate(a, b)
    adjacency_list[a].append((b, dist))
    #distance도 넣어야 함?
print(adjacency_list)
print(nodes_position)
def dijkstra(start):
    q = []
    additional_line = 0
    x, y = nodes_position[start]
    heapq.heappush(q, (start, x, y))
    while q:
        #미리 M 거리상의 모든 node와의 거리를 계산해둬야 하나..
        
        node, i, j = heapq.heappop(q)
        #연결된 노드가 없을 경우
        if len(adjacency_list[node]) == 0:
        
        #연결된 노드가 이미 있을 경우
        for adj in adjacency_list[node]:
            if 
        
dijkstra(1)

#dijkstra 구현
# import sys
# import math
# input = sys.stdin.readline

# N, W = map(int, input().split())
# M = float(input())

# nodes_position = []
# nodes_conn = []
# for _ in range(N):
#     nodes_position.append(list(map(int, input().split())))

# #모든 node에 대해서
# default_map = [[1e9 for _ in range(N)] for _ in range(N)]

# def calculate(x, y):
#     i, j = nodes_position[x]
#     ii, jj = nodes_position[y]
#     return math.sqrt(abs(i-ii)+ abs(j-jj))

# for _ in range(W):
#     x, y = map(int, input().split())
#     nodes_conn.append((x, y))
#     default_map[x-1][y-1] = calculate(x-1, y-1)

# # 1번 부터 ~ N번 까지 (최단 추가 거리 저장)
# distance_map = [1e9 for _ in range(N)]

