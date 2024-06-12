import sys
input = sys.stdin.readline

N = int(input())
consulting = [tuple(map(int,input().split())) for _ in range(N)]

result = 0

#넣고 안넣고로 바꿔줘야 함!!
def backtracking(x,total):
    time, pay = consulting[x]
    if x+time >= N:
        return
    #넣고
    total += pay
    for j in range(x+1, N):
        backtracking(j, total)
    total -= pay
    for j in range(x+1, N):
        backtracking(j,total)

    return total
    #안넣고

total = 0
for i in range(N):
    #dp = [0 for i in range(N)]
    #result = max(result, backtracking(dp, i, total))
    result = max(result, backtracking(i,total))

    # time, pay = consulting[i]
    # if i+time < N:
    #     for x in range(time):
    #         dp[i+x] = pay
    # for j in range(i+1,N):
    #     t, p = consulting[j]
    #     if dp[j] != 0:
    #         continue
    #     elif j+ t > N:
    #         continue
    #     else:
    #         tmp = dp[j-1]+ p
    #         for y in range(t):
    #             dp[j+y] = tmp
            # if i == 0:  
            #     for y in range(t):
            #         dp[j+y] = p
            # else:
            #     tmp = dp[j-1]+ p
            #     for y in range(t):
            #         dp[j+y] = tmp
    #print(dp)
    #result = max(result, max(dp))
    print(result)
