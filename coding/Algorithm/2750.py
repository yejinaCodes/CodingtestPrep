import sys
import heapq

input = sys.stdin.readline

N = int(input())

heap = []
for i in range(N):
    x = int(input())
    heapq.heappush(heap, x)

for i in range(N):
    print(heapq.heappop(heap))
