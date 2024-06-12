import sys
input = sys.stdin.readline

N,M = map(int,input().split())

Time = []
for i in range(N):
    Time.append(int(input()))

Time.sort()
start = 0
end = Time[-1] * M

result = 0

while start <= end:
    count = 0 
    mid = (start+end)//2

    for value in Time:
        count += (mid//value)

        #이미 count가 m개수를 초과했을 때 더이상 계산하지 않아도 됨.
        if count >= M:
            break
    #print(count)

    #Count가 M이상일 경우 이미 조건 만족이므로 result에 mid값을 저장해준다.
    if count >= M:
        result = mid
        end = mid-1

    else:
        #result = mid
        start = mid+1

print(result)