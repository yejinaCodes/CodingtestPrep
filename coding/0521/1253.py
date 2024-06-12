import sys
input = sys.stdin.readline

N = int(input())
nums = sorted(list(map(int, input().split())))
# nums.sort(reverse=True)

result = 0
#range를 두면 안됨!!
for i in range(N):
    isgood = nums[i]
    left = 0 # 전체를 봐야하기 떄문
    right = N - 1
    while left < right:
        tmp = nums[left] + nums[right]
        if tmp == isgood: 
            if i == left: # 자기 자신을 count하면 안되기 때문
                left += 1
            elif i == right:
                right -= 1
            else:
                result += 1
                break
            #and i != left:
            # result += 1
        elif tmp < isgood:
            left += 1
        elif tmp > isgood:
            right -= 1

print(result)

# for i in range(N-2):
#     fixed = nums[i]
#     left = i + 1
#     right = N - 1
#     while left < right:
#         tmp = nums[left] + nums[right]
#         if tmp < fixed:
#             right -= 1
#         elif tmp > fixed:
#             left += 1
#         else:
#             result.add(fixed)
#             right -= 1
# print(len(result))