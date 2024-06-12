import sys
import heapq
input = sys.stdin.readline

N = int(input())
lines = []
for i in range(N):
    lines.append(list(map(int, input().split())))

lines.sort(key = lambda x:(x[0], x[1]))

process = [[lines[0][0], lines[0][1]]]
#left = lines[0][0]
#right = lines[0][1]

answer = 0

# for i in range(1, N):
#     if right >= lines[i][1]:
#         continue
#     elif lines[i][0] <= right < lines[i][1]:
#         right = lines[i][1]
#     elif right < lines[i][0]:
#         answer += right - left
#         left = lines[i][0]
#         right = lines[i][1]

# answer += right - left
# print(answer)

for i in range(1, N):
    #print(process)
    if lines[i][0] <= process[0][1]:
        if lines[i][1] > process[0][1]:
            process[0][1] = lines[i][1]
    else:
        answer += process[0][1] - process[0][0]
        process = [[lines[i][0], lines[i][1]]]
        #heapq.heappush(process, [lines[i][0], lines[i][1]])

#for line in process:
#    answer += line[1] - line[0]
answer += process[0][1] - process[0][0]

print(answer)