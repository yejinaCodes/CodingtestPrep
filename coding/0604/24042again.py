#언제 maxsize 사용하고 언제 1e9사용하는지 정확히 알기: 시간복잡도를 계산했을 때 최악의 경우가 1e9보다 크다.

'''
불이 켜지는 시간들은 등차수열을 이룬다.
식: i+(N-1)*M 이다.
지나가려면 횡단보도에 불이 켜지는 시간은 항상 현재 시간 이상이여야 한다.
time <= i+(N-1)*M
(time-i)/M <= N-1

즉, N-1은:
time-i가 M으로 나우어서 떨어지면 (time-i)//M
아니면 (time-i)//M+1
'''

'''
두 노드를 연결하는 비용은 주기를 계산해 얻어낼 수 있다. 이동 가능한 다음 주기는 현재 시간보다 값이 커야
한다는 점이다. %를 사용해 주기를 카운트하고 이동시간 1을 포함해 djikstra로 구현하기.
'''

import heapq
import sys
input = sys.stdin.readline
N, M = map(int, input().split())

arr = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split()) #횡단보도니깐 양방향
    arr[a].append((b, i))
    arr[b].append((a, i))

def dijkstra():
    distances = [sys.maxsize for _ in range(N+1)]
    distances[1] = 0
    pq = []
    heapq.heappush(pq, [0, 1]) #time, node

    while pq:
        time, node = heapq.heappop(pq)
        if distances[node] < time:
            continue
        if node == N:
            return time
        for nxt_node, nxt_time in arr[node]:
            nxt_cost = time + (nxt_time - time) % M
            #time = 현재 시간
            #(nxt_time-time)%M = 주기 카운트
            if distances[nxt_node] > nxt_cost + 1:
                distances[nxt_node] = nxt_cost + 1
                heapq.heappush(pq, [nxt_cost+1, nxt_node])
    return distances[N]

answer = dijkstra()
print(answer)


# def dijkstra():
#     q = []
#     heapq.heappush(q, (0, 1))
#     distance = [sys.maxsize for _ in range(N+1)]
#     distance[1] = 0
#     while q:
#         time, node = heapq.heappop(q)
#         if node == N:
#             return time
#         if distance[node] < time:
#             continue
#         for i, nnode in arr[node]:
#             if (time - i) % M == 0:
#                 ntime = i + ((time - i)//M) * M
#             else:
#                 ntime = i + ((time - i)//M+1)*M
            
#             if distance[nnode] > ntime + 1:
#                 distance[nnode] = ntime + 1
#                 heapq.heappush(q, (ntime+1, nnode))