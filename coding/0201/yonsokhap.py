import sys
input = sys.stdin.readline
#sys.stdin = open('./0201/yonsokhap.txt')

n = int(input())
nums = list(map(int,input().split()))

dp = [0] * n
dp[0] = nums[0]

for i in range(1,n):
    dp[i] = max(nums[i], dp[i-1]+nums[i])

print(max(dp))

    # check = 0
    # for j in range(i):
    #     check = max(nums[j], nums[j]+ nums[j-1])

# for i in range(n-1):
#     dp[i] = nums[i] + nums[i+1]


# for i in range(n):
#     result = nums[i]
#     for j in range(n):
#         if nums[i]+ dp[j] > result:
#             result = nums[i]+dp[j]

# print(max(dp))     

# for i in range(n):
#     check = 0
#     #print(i)
#     for j in range(n-i):
#         #print(j)
#         if check+nums[i+j] > dp[i]:
#             #print(check+nums[j])
#             dp[i] = check+nums[i+j]
#         #check = max(check, check+nums[j])
#         check += nums[i+j]

# print(max(dp))