import sys
input = sys.stdin.readline

N = int(input())
lectures = []
for i in range(N):
    lectures.append(list(map(int, input().split())))


lectures.sort(key = lambda x:(x[1], x[0]))
count = 1
end = lectures[0][1]
for i in range(1, N):
    if lectures[i][0] >= end:
        count += 1
        end = lectures[i][1]

print(count)
            

# lectures.sort(key = lambda x:(x[0], x[1]))

# result = 0

# def backtracking(end, count, position):
#     global result
#     if position >= N:
#         result = max(result, count)
#         #print(count)
#         return
#     for _ in range(position, N):
#         if lectures[_][0] >= end:
#             backtracking(lectures[_][1], count+1, _+1)

# for i in range(N):
#     backtracking(lectures[i][1], 0, i+1)

# print(result)