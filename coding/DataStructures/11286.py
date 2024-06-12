#우선순위 힙 어떻게 하지?
#tuple로 넣을 경우 (x,y) x를 기준으로 min heap 정렬됨. 만약에 x가 같을경우 작은 y를 기준으로
#정렬됨.

import sys
import heapq

input = sys.stdin.readline

n = int(input())
answer = []

#내 방법도 맞았음! :)
        
result = []

for i in range(n):
    check = int(input())

    if check == 0:
        if len(answer) == 0:
            result.append(0)
        else:
            value,plusmin = heapq.heappop(answer)
            result.append(value*plusmin)
            # if plusmin == -1:
            #     result.append(value*plusmin)
            # else:
            #     result.append(value)
    else:
        if check < 0:
            heapq.heappush(answer, (abs(check), -1))
        else:
            heapq.heappush(answer, (check,1))

for i in result:
    print(i)



# result = []

# for i in range(n):
#     check = int(input())
#     if check == 0:
#         if len(answer) == 0:
#             result.append(0)
#         else:
#             value,plusmin = heapq.heappop(answer)
#             result.append(plusmin)
#     else:
#         heapq.heappush(answer, (abs(check), check))
#     print(answer)