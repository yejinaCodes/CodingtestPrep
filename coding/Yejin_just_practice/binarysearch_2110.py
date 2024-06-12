#구간 mid 거리 기준으로 M개의 설치 가능 확인
#여기서 중요한 포인트는 각 homes의 구간 거리가 아니라 homes에 위치한 공유기와의
#그 다음 공유기 위치와의 거리를 참고해야 한다는 점!!
#난 그래서 여기서 pointer를 사용해서 공유기가 있는 위치를 저장해주었음.


import sys
input = sys.stdin.readline

N, M = map(int,input().split())
homes = []
for i in range(N):
    homes.append(int(input()))
homes.sort()

start = 1
end = max(homes)-min(homes)
result = 0

#pointer = 0
while start <= end:
    count = 0
    mid = (start+end)//2
    pointer = 0
    #print(mid)
    for i in range(1, len(homes)):
        if i <= pointer:
            #print('check')
            #print(i)
            #print('h')
            #print(pointer)
            continue
        if (homes[i]-homes[pointer] >= mid):
            #print('cc')
            #print(i)
            count += 1
            pointer = i
    count += 1
    #print('count')
    #print(count, mid)
    if count >= M:
        result = mid
        start = mid+1
    else:
        end = mid-1
    
print(result)