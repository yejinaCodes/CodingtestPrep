import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
#양방향 리스트
adjacency_list = [[] for _ in range(N+1)]

sequence = deque([] for _ in range(M+1)) #신호동 순서

for i in range(M):
    a, b = map(int, input().split())
    adjacency_list[a].append((b, i+1))
    sequence[i].append((a,b)) #뽑아쓸때는 (a,b), (b,a) 둘다 사용
    adjacency_list[b].append((a, i+1))

# print(sequence)
answer = 1e9

def dijkstra(x, t):
    global answer
    q = deque()
    result = [1e9 for _ in range(N+1)]
    #print(result)
    q.append((x, t))
    while q:
        now, time = q.popleft()
        if now == N:
            result[now] = min(result[now], time)
            answer = result[now-1]
        for city, ttime in adjacency_list[now]:
            # print(city)
            time += ttime
            if result[city] >= time:
                result[city] = time
                q.append((city, time))
    
    print(result)

dijkstra(1, 0)
print(answer)
