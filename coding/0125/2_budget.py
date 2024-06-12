#binary search
#중복값이 있을 경우, 없을 경우
#백준2512
#"매개변수 탐색문제"
import sys
sys.stdin = open('./0125/budget_input.txt')

num_req = int(input())
budget_req = sorted(list(map(int, input().split())))
country_budget = int(input())

#각 에상요청에 줄수 있는 상한금액이 max(budget_req)일 것이기 때문
start, end = 0, max(budget_req)

answer = 0
#binary로 서치하기
#start,end는 상환값의 경우의 수인데 거기에서 제일 크지만 국가예산을 넘지 않는 값이기 때문이다.
while start <= end:
    #여기에서 medium은 index가 아니라 budget_req에서의 medium값이다.
    medium = (start+end)//2
    total = 0
    for i in budget_req:
        total += min(i, medium)
    if total <= country_budget:
        start = medium + 1
        answer = medium
    else:
        end = medium - 1

print(answer)

