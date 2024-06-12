#가운데를 말해요
import sys
import heapq
input = sys.stdin.readline

N= int(input())

# data = []
# for i in range(N):
#     data.append(int(input()))

# med_ian = data[0]
# result = [med_ian]

left_heap = []
right_heap = []

for i in range(N):
    data = int(input())

    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, -data)
    else:
        heapq.heappush(right_heap, data)
    
    if right_heap and (left_heap[0]*-1) > right_heap[0]:
        left = heapq.heappop(left_heap)
        right = heapq.heappop(right_heap)
        heapq.heappush(right_heap, -left)
        heapq.heappush(left_heap, -right)
    print(left_heap[0]*-1)


# for i in range(1, N):
    
#     if data[i] < med_ian:
#         heapq.heappush(left_heap, -data[i])
#     elif data[i] > med_ian:
#         heapq.heappush(right_heap, data[i])
#     #홀수일 경우
#     if i%2 == 0:
#         if len(left_heap) > len(right_heap):
#             heapq.heappush(right_heap, med_ian)
#             med_ian = -heapq.heappop(left_heap)

#             #result.append(med_ian)
#         elif len(left_heap) < len(right_heap):
#             heapq.heappush(left_heap, -med_ian)
#             med_ian = heapq.heappop(right_heap)
#             #result.append(med_ian)    
    
#     #짝수일 경우
#     else:
#         # if len(left_heap) < len(right_heap):        
#         #     #result.append(med_ian)
#            # print(result)
#         if len(left_heap) > len(right_heap):
#             heapq.heappush(right_heap, med_ian)
#             med_ian = -heapq.heappop(left_heap)
#             #result.append(med_ian)

    
#     result.append(med_ian)

# for i in result:
#     print(i)