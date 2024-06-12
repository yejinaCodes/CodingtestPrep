#누적합을 사용해야 함
import sys
from copy import deepcopy
#기존 리스트 유지를 위해 deepcopy사용

input = sys.stdin.readline
n = int(input())
honey = list(map(int,input().split()))

s = deepcopy(honey)
result = 0

#누적합 미리 구해놓기
for i in range(1, n):
    s[i] += s[i-1]


#3가지의 경우의 수를 모두 계산하기
#1. 양끝에 벌꿀과 꿀통이 고정일 경우. 오른쪽이 꿀통일 경우
for i in range(1, n-1):
    #벌위치 2개 빼주기
    #2*s[-1]에서 누적합이 더해줬을 테니깐 s[i]로 빼줘야 함. 
    result = max(result, 2*s[-1]- honey[0] - honey[i] - s[i])

#2. 양끝에 벌꿀과 꿀통이 고정일 경우. 왼쪽이 꿀통일 경우
for i in range(1, n-1):
    #오른쪽 꿀벌 = s[-1] - honey[-1] - honey[i]
    #중간어딘가의 꿀벌 = s[i-1]
    result = max(result, s[-1] - honey[-1] - honey[i] + s[i-1])

#3. 벌꿀이 양쪽에 고정일 경우. 
for i in range(1, n-1):
    #벌통이 왔다갔다 함
    #왼쪽벌꿀에서 벌통까지: s[i] - honey[0]
    #오른쪽벌꿀에서 벌통까지: s[-1] - honey[-1] - s[i-1]
    result = max(result, (s[i]-honey[0])+(s[-1]-honey[-1]-s[i-1]))

print(result)