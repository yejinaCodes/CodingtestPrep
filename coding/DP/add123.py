# #패턴 구하고, 점화식 구하기

import sys
input = sys.stdin.readline

nums = []
T = int(input())
for testcase in range(T):
    nums.append(int(input()))

result = []

for num in nums:
    dp=[0]*num
    dp[0]=1
    dp[1]=2
    dp[2]=4
    for i in range(3, num):
        dp[i] = dp[i-1]+dp[i-2]+dp[i-3]

    result.append(dp[-1])

for i in result:
    print(i)


########################

import sys
input = sys.stdin.readline

T = int(input())
result = []

for testcase in range(T):
    n = int(input())
    dp=[0]*(n+1)
    
    for i in range(1, n+1):
        if i == 1:
            dp[i] = 1
        elif i == 2:
            dp[i] = 2
        elif i == 3:
            dp[i] = 4
        else:
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    result.append(dp[n])

for i in result:    
    print(i)