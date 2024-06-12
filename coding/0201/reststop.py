import sys
input = sys.stdin.readline

n,m,l = map(int,input().split())
rest_stops = list(map(int,input().split()))

rest_stops.append(0)
rest_stops.append(l)
rest_stops.sort()

#0 과 l위치에는 휴게소를 설치할 수 없기 때문
start = 1
end = l-1
result = 0 

#구간 거리 리스트 만들지 않아도됨.
# for i in range(len(rest_stops)):

while start <= end:
    count_stops_possible = 0
    mid = (start + end)//2
    for i in range(1, len(rest_stops)):
        if rest_stops[i]-rest_stops[i-1] > mid:
            count_stops_possible += (rest_stops[i]-rest_stops[i-1]-1)//mid
    if count_stops_possible > m:
        start = mid+1
    else:
        end = mid-1
        result = mid
    
print(result)

        #작을 경우에는 설치를 못하기 때문에 클경우만 계산한다.
            #rest_stops[i]-rest_stops[i-1]에서 이미 설치 되어있는 구역 1개를 추가해서 카운트 된것이기 때문에 -1해줘야 한다. 
        #같거나 작을 경우일때 result에 저장해주어야함.
        #조건만족은 했기 때문에 result에 저장.

'''
#휴게소 간격 최대값을 정하기 . 
#최대값 '간격'을 줄이거나 키우는 방법으로 최적의 값을 이진분법을 통해서 찾기 

import sys
import math

input = sys.stdin.readline
n,m,finish = map(int,input().split())
stop = list(map(int,input().split()))

if 0 not in stop:
    stop.append(0)
if finish not in stop:
    stop.append(finish)
stop.sort()
#print(stop)

while m > 0:
    stop.sort()
    highway = 0
    nextstop = 0
    for i in range(len(stop)-1):
        #최대값 구하기
        location = stop[i+1] - stop[i]
        #round((stop[i]+stop[i+1])/2)
        if location > highway:
            highway = location
            nextstop = round((stop[i]+stop[i+1])/2)
        
    # if m  == 1:
    #     # print(highway)
    #     # print(round(highway/2)+1)
    #     break

    if nextstop == 0 or nextstop == finish:
        continue
    else:
        stop.append(nextstop)
        m-=1
        #print(stop)

stop.sort()
print(stop)
result = 0
for i in range(len(stop)-1):
    location = stop[i+1]-stop[i]
    if location > result:
        result = location
print(result)

'''