import sys
input = sys.stdin.readline

n = int(input())
stairs = [0] * (n+1)
for i in range(1, n+1):
    stairs[i] = int(input())

#dp는 해당 i위치 까지 오는데 밟는 계단의 최대값이 저장되어 있음.
#n+1로하면 runtime error 떠서 301로 바꿔줘야 함.
dp = [0] * (n+1)
#dp 초기화하기
#점화식이 이전 값들에 대해 참고하기 떄문에 dp 초기화에는 dp[3] 까지의 값이 들어가 있어야 한다.
dp[1] = stairs[1]
#이 부분이 조금 헷갈릴 수도 있음.
dp[2] = stairs[1] + stairs[2]
dp[3] = max(stairs[1]+stairs[3], stairs[2]+stairs[3])

#점화식
#직전 칸에서 올라왔을 경우
#전전 칸에서 올라왔을 경우
#둘 중 max값을 dp[i] 위치에 저장.
for i in range(4, n+1):
    dp[i] = max(stairs[i]+stairs[i-1]+dp[i-3], stairs[i]+dp[i-2])

print(dp[n])