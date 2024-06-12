import sys
from collections import deque
import heapq
input = sys.stdin.readline

N = int(input())
table = [[] for _ in range(N * N + 1)]
order = []
positions = []

for i in range(N * N):
    tmp = list(map(int, input().split()))
    table[tmp[0]] = (tmp[1:])
    order.append(tmp[0])

result = [[0 for _ in range(N)] for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1] 


for i in range(len(order)):
    #첫번째일 경우 항상 1,1에 지정하기
    if i == 0:
        result[1][1] = order[i]
        positions.append((1, 1))
    
    else:
        tmp = set()
        for x in range(len(positions)):
            i, j = positions[x]
            if result[i][j] in table[order[i]]:
                for d in range(4):
                    nx = dx[d] + i
                    ny = dy[d] + j
                    if nx < 0 or nx >= N or ny < 0 or ny >= N:
                        continue
                    if result[nx][ny] == 0:
                        tmp.add((nx, ny))

        maxheap = []
        for c in tmp:
            t = []
            friends = 0
            empty = 0
            for d in range(4):
                nx = dx[d] + c[0]
                ny = dy[d] + c[1]
                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    continue
                if result[nx][ny] == 0:
                    empty += 1
                elif result[nx][ny] in table[order[i]]:
                    friends += 1
            maxheap.append([friends, empty, c[0], c[1]])
            #heapq.heappush(maxheap, -())
        maxheap.sort(key = lambda x:(-x[0], -x[1], x[2], x[3]))
        print(maxheap[0][2], maxheap[0][3])
        #friends, empty, x, y = -heapq.heappop(maxheap)
        result[maxheap[0][2]][maxheap[0][3]] = order[i]

        
print(result)
