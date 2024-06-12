import sys
input = sys.stdin.readline

N = int(input())
negative_and_zero = []
positive = []
answer = 0

for i in range(N):
    tmp = int(input())
    if tmp <= 0:
        negative_and_zero.append(tmp)
    elif tmp > 1:
        positive.append(tmp)
    else:
        answer += tmp

negative_and_zero.sort()
positive.sort(reverse = True)

#짝수
for i in range(0, len(positive), 2):
    if (i + 1) >= len(positive):
        answer += positive[i]
    else:
        answer += positive[i] * positive[i+1]

#홀수
for i in range(0, len(negative_and_zero), 2):
    if (i + 1) >= len(negative_and_zero):
        answer += negative_and_zero[i]
    else:
        answer += negative_and_zero[i] * negative_and_zero[i+1]

print(answer)




# #짝수일 경우:
# if len(negative_and_zero)%2 == 0:
#     for i in range(0, len(negative_and_zero), 2):
#         answer += negative_and_zero[i] * negative_and_zero[i+1]
# #홀수일 경우:
# elif len(negative_and_zero)%2 != 0:
#     for i in range(0, len(negative_and_zero)-1, 2):
#         answer += negative_and_zero[i] * negative_and_zero[i+1]
#     answer += negative_and_zero[-1]

# #짝수일 경우:
# if len(positive)%2 == 0:
#     for _ in range(0, len(positive), 2):
#         if positive[_] == positive[_+1] and positive[_] == 1:
#             answer += 2
#             continue
#         answer += positive[_] * positive[_+1]
        
# #홀수일 경우:
# elif len(positive)%2 != 0:
#     for _ in range(0, len(positive), 2):
#         if positive[_] == positive[_+1] and positive[_] == 1:
#             answer += 2
#             continue
#         answer += positive[_] * positive[_+1]
#     answer += positive[-1]

# print(answer)