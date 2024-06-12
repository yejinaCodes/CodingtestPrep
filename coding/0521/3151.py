import sys
input = sys.stdin.readline

N = int(input())
scores = sorted(list(map(int, input().split())))

answer = 0

for i in range(N-2):
    left, right = i+1, N-1
    student = -scores[i]
    mx_idx = N
    while left < right:
        tmp = scores[left] + scores[right]
        if tmp < student:
            left += 1
        elif tmp == student:
            if scores[left] == scores[right]:
                answer += right - left
            else:
                #left 원소와 right 원소가 다를 경우
                if mx_idx > right:
                    mx_idx = right
                    while mx_idx >= 0 and scores[mx_idx-1] == scores[right]:
                        mx_idx -= 1
                answer += right - mx_idx + 1
            left += 1
        else:
            right -= 1
print

'''
teams = set()
for i in range(N-2):
    student = -scores[i] # 다른 2개의 합이 student의 음수값이여야지 총 값이 0이된다.
    left = i + 1
    right = N - 1
    while left < right:
        tmp = scores[left] + scores[right]
        if tmp < student:
            left += 1
        elif tmp > student:
            right -= 1
        else:
            team = tuple(sorted((i, left, right)))
            teams.add(team)
            left += 1

print(len(teams))

'''



# teams = set()
# for i in range(N):
#     student = scores[i]
#     left = 0
#     right = N-1
#     while left < right:
#         tmp = scores[left] + scores[right] + student
#         #print(tmp)
#         if tmp == 0:
#             if i == left:
#                 left += 1
#             elif i == right:
#                 right -= 1
#             else:
#                 team = tuple(sorted((i, left, right)))
#                 #print(team)
#                 teams.add(team)
#                 right -= 1
#                 #break
#         elif tmp < 0:
#             left += 1
#         elif tmp > 0:
#             right -= 1

# print(len(teams))