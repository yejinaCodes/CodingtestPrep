import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())
cards = list(map(int, input().split()))
heapq.heapify(cards)
#print(cards)
for i in range(M):
    first = heapq.heappop(cards)
    second = heapq.heappop(cards)
    tmp = first + second
    heapq.heappush(cards, tmp)
    heapq.heappush(cards, tmp)

print(sum(cards))
