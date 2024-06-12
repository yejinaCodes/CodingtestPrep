
import sys
input = sys.stdin.readline

n,s = map(int,input().split())
nums = list(map(int,input().split()))

sum = 0
leftpointer = 0
rightpointer = 0
answer = 1e9

#left가 right와 교차하는 일이 일어나면 안됨.
while True:
    if sum>= s:
        answer = min(answer, rightpointer-leftpointer)
        sum -= nums[leftpointer]
        print(answer)
        leftpointer += 1
    elif rightpointer == n:
        break
    else:
        sum += nums[rightpointer]
        rightpointer += 1

if answer == 1e9:
    print(0)
else:
    print(answer)


# for i in range(n):
#     if i == 0 and nums[i] >= s:
#         print(1)
#         sys.exit()
#     if i == rightpointer:
#         rightpointer += 1

#     if nums[i] + nums[rightpointer] >= s:
#         answer = min(answer, rightpointer-i+1)
#         print(i, rightpointer, answer)
#         continue
#     else:
#         rightpointer += 1

# print(answer)
