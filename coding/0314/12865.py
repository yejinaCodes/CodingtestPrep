
# #모든 경우의 수를 재귀로 찾을 수 어렵다
# #예)
# #(5, 9)
# #(2,4),(2,3),(2,5),(3,1),(3,10)

# #DP를 사용해야 함
# import sys
# from copy import deepcopy
# input = sys.stdin.readline

# N, K = map(int,input().split())
# things = []
# for i in range(N):
#     w, v = map(int,input().split())
#     things.append((w,v))

# things = sorted(things, key=lambda x:(x[0], x[1]))
# dp = [[0,0]]*N
# answer = 0 

# check = K
# #예외케이스 처리하기
# if things[0][1] <= K:
#     dp[0] = things[0]
#     check -= dp[0][0]
#     answer = things[0][1]
# else:
#     print(0)
#     sys.exit()
# print(dp)
# print(answer)

# #dp 초기화
# for i in range(1, N):
#     check = check- things[i][0]
#     #print(check)
#     if check >= 0:
#         value = things[i][1] + dp[i-1][1]
#         weight = dp[i-1][0] + things[i][0]
#         dp[i] = (weight, value)
#         answer = max(answer, dp[i][1])
#     else:
#         check = i
#         break

# print(dp)
# print(answer)

# for i in range(check, N):
#     value = 0
#     #ccheck = things[i][1]
#     tmpK = K
#     weight = 0
#     for x in range(i, -1, -1):
#         if tmpK == 0 or tmpK < 0:
#             break
#         #max비교하는 연산이 필요할 것 같음...

#         #tmpK -= things[i][0]
#         if tmpK-things[i][0] >= 0:
#             tmpK-= things[i][0]
#             weight += things[i][0]
#             value += things[i][1]
    
#     dp[i] = (weight, value) 
#     answer = max(answer, dp[i][1])

#     #answer = max(answer, dp[i][1])
#     #print(answer)
#         # if tmpK-things[i][0]-things[i-1][0] >= 0:
#         #     tmpK = tmpK-things[i][0]-things[i-1][0]
#         #     weight = things[i][0] + things[i-1][0]
#         #     value = things[i][1] + things[i-1][1]
#         #     dp[i] = (weight,value)

# print(dp)
# print(answer)
# #print(max(dp))
# #print(dp[-1][1])


import sys
input = sys.stdin.readline

N,K = map(int,input().split())
things = [(0,0)]
for i in range(N):
    w,v = map(int,input().split())
    things.append((w,v))

dp = [[0]*(K+1) for _ in range(N+1)]

answer = 0


#dp[i][j] 로 j크기의 무게를 접근하기 위해 index의 크기를 1개씩 늘려야 한다.
for i in range(1, N+1):
    
    weight = things[i][0]
    value = things[i][1]

    for j in range(1, K+1):
        
        #크거나 같을 때여야 함.
        if j >= weight:
            #해당 물건을 넣을 수 있음
            #넣을때 이전에 넣은 물건의 가치가 높은거 이전 물건을 넣고
            #아닐 경우, 해당 물건의 가치를 j-weight 까지의 최대값과 더해준다.
            dp[i][j] = max(dp[i-1][j], value + dp[i-1][j-weight])
        
        elif j < weight:
            dp[i][j] = dp[i-1][j]


        # else:
        #     dp[i][j] = max(value, dp[i-1][j])


print(dp[N][K])
    