#최대 무게는 정해져 있고
#어떻게 물건을 넣어야지 최대값을 얻을지가 포인트이다.

#물건 하나를 넣고 현재 가치 저장 + k-w 를 더 넣을 수 있다로 생각 전환

#최대이익[i][w] 
#= 최대무게가 w인 가방에서 i번째 물건까지 판단했을 때의 최대 가치

#dp 2차원 배열 사용하기
import sys
input = sys.stdin.readline

n,k = map(int,input().split())

chart = [[0]*(k+1) for _ in range(n+1)]
things = [(0,0)]


for i in range(n):
    w,v = map(int,input().split())
    things.append((w,v))

for i in range(1, n+1):
    for j in range(1, k+1):
        w = things[i][0] 
        v = things[i][1]

        if j < w:
            chart[i][j] = chart[i-1][j]
        
        else:
            chart[i][j] = max(chart[i-1][j], v+chart[i-1][j-w])

print(chart[n][k])