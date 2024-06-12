# import sys
# import heapq
# input = sys.stdin.readline


# heap = []

# check = list(str(input().rstrip("][\n")))
# for i in range(len(check)):
#     heapq.heappush(heap, -int(check[i]))

# for i in range(len(heap)):
#     print(-heapq.heappop(heap), end='')

#정렬로 풀기

import sys

# input = sys.stdin.readline

x = input()

for i in range(9,-1,-1):
    for j in x:
        if int(j) == i:
            print(i, end='')
        