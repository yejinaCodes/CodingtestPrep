import sys
import heapq
input = sys.stdin.readline

N = int(input())
classes =[]

count = 0

for i in range(N):
    classes.append(list(map(int, input().split())))

classes.sort(key = lambda x: (x[0], x[1]))

process = [classes[0][1]]

for i in range(1, N):
    if classes[i][0] >= process[0]:
        heapq.heappop(process)
    heapq.heappush(process, classes[i][1])

print(len(process))

# for i in range(N):
#     if len(process) == 0:
#         heapq.heappush(process, classes[i][1])
#     else:
#         for _ in range(len(process)):
#             #if process[-1] > classes[i][0]:
#             #    heapq.heappush(process, classes[i][1])
#             #    break
#             tmp = heapq.heappop(process)
#             if classes[i][0] >= tmp:
#                 heapq.heappush(process, classes[i][1])
#                 break
#             heapq.heappush(process, tmp)
#             heapq.heappush(process, classes[i][1])

# print(len(process))
                    

# for i in range(N):
#     process.sort()
#     if len(process) == 0:
#         process.append(classes[i][1])
#     else:
#         for j in range(len(process)):
#             if classes[i][0] >= process[j]:
#                 #print(process[j])
#                 process.remove(process[j])
#                 process.append(classes[i][1])
#                 break
#             else:
#                 process.append(classes[i][1])
#                 break
#     #print(process)

# print(len(process))