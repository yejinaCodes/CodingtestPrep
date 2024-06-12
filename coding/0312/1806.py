# import sys
# from collections import deque
# iput = sys.stdin.readline
# N, S = map(int,input().split())
# Ss = list(map(int,input().split()))

# SumS = [0 for i in range(N)]
# SumS[0]= Ss[0]
# if Ss[0] >=S:
#     print(1)
#     sys.exit()
# for i in range(1, N):
#     if Ss[i] >= S:
#         print(1)
#         sys.exit()
#     SumS[i] = Ss[i] + SumS[i-1]
# answer = 10e9
# left_pointer = 0
# right_pointer = 0

# #left right 교차부분이 문제
# while True:
#     if right_pointer >= N:
#         break    
#     if abs(SumS[right_pointer] - SumS[left_pointer]) < S:
#         right_pointer += 1
#     elif abs(SumS[right_pointer] - SumS[left_pointer]) >= S:
#         answer = min(answer, right_pointer-left_pointer+1)
#         if left_pointer == right_pointer:
#             right_pointer += 1
#         left_pointer += 1

# if answer == 1e9:
#     print(0)
# else:
#     print(answer)

import sys
input = sys.stdin.readline

N,S = map(int,input().split())
nums = list(map(int,input().split()))

leftpointer = 0
rightpointer = 0
sum = 0
answer = 1e9

while True:
    #sum을 보존하면서 반복 계산을 막아준다.
    #leftpointer should not pass rightpointer
    if sum >= S:
        #이전 if문에서 이미 rightpointer를 옮겨주었기 때문에 여기서는 그냥
        #rightpointer-leftpointer하면 된다.
        answer = min(answer, rightpointer-leftpointer)
        print(answer)
        sum -= nums[leftpointer]
        leftpointer += 1

    elif rightpointer == N:
        break

    else:
        sum += nums[rightpointer]
        rightpointer += 1

if answer == 1e9:
    print(0)
else:
    print(answer)