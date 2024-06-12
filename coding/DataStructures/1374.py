#강의실 문제

import sys
import heapq

input = sys.stdin.readline

N = int(input())

heap_classes_end = []

times = []

for i in range(N):
    name, start, end = map(int,input().split())
    heapq.heappush(times, (start,end))


start,end = heapq.heappop(times)
heapq.heappush(heap_classes_end, end)
count = 1

for i in range(N-1):
    #print(i)
    new_start,new_end = heapq.heappop(times)
    end = heapq.heappop(heap_classes_end)

    if new_start < end:
        heapq.heappush(heap_classes_end, end)
        heapq.heappush(heap_classes_end, new_end)
        count += 1
    else:
        heapq.heappush(heap_classes_end, new_end)


print(count)

# print(classes)
# while len(times) > 0:
#     start,end = heapq.heappop(times)
#     #print(start,end)
#     #가장 빨리 끝나는 시간을 찾아야 함...
#     for i in range(len(classes)):
#         if start > classes[i]:
#             classes[i] = end
#             break
#         elif classes[i] == 10e9:
#             classes[i] = end
#             count +=1
#             break
#         else:
#             continue

# print(count)