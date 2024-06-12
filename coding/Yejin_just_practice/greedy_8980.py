# import sys
# import heapq
# input = sys.stdin.readline

# stops, weight = map(int, input().split())
# m = int(input())
# stops_info = []
# for i in range(m):
#     stops_info.append(list(map(int, input().split())))

# stops_info.sort(key=lambda x:(x[0], x[1]))
# #print(stops_info)

# result = 0
# tmp = []
# current_weight = weight

# for i in stops_info:
#     min_box = weight
#     for j in range(i[0], i[1]):
#         min_box = min(min_box, )


# # for i in range(1, stops):
# #     #get
# #     tmp = 

# # for i in range()

import sys
from collections import deque
input = sys.stdin.readline

N, C = map(int, input().split())
M = int(input())
infos = []
for _ in range(M):
    start, end, nums = map(int, input().split())
    infos.append([start, end, nums])

infos.sort(key=lambda x:x[1])
Trucks_C = [C]* N
res = 0 
for s,r,box in infos:
    min_c = C
    for i in range(s, r):
        if min_c > min(Trucks_C[i], box):
            min_c = min(Trucks_C[i], box)
    
    for i in range(s, r):
        Trucks_C[i] -= min_c
    res += min_c

print(res)



