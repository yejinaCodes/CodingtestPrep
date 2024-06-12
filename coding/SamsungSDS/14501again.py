# import sys
# input = sys.stdin.readline

# N = int(input())
# consulting = [list(map(int,input().split())) for i in range(N)]
# dp = [0 for _ in range(N+1)]

# for i in range(N-1, -1, -1):
#     if i + consulting[i][0] > N:
#         dp[i] = dp[i+1]
#     else:
#         dp[i] = max(dp[i+1], consulting[i][1] + dp[])

import sys
input = sys.stdin.readline

N = int(input())

consulting = [list(map(int,input().split())) for i in range(N)]
dp = [0 for i in range(N+1)]

#넣고 안넣고 할 수 있기 떄문..

#i번째까지 일했을 때 얻는 최대 수익을 계산하는 기준으로
#dp[i]는 i번째날까지 일을 했을 때, 최대값이다.
for i in range(N):
    #i번째 날에 상담을 진행했을 때, 이후 상담 가능한 모든 날짜를 뜻함. 
    for j in range(i+consulting[i][0], N+1):
        #print('check', i, j)
        #print(dp)
        if dp[j] < dp[i] + consulting[i][1]:
            dp[j] = dp[i] + consulting[i][1]
        #print('cc')
        #print(dp)

print(dp[-1])