
#lower bound/upper bound


import sys
sys.stdin = open('./0125/3_cutLAN.txt')

k,n = map(int, input().split())
lans = []
for i in range(k):
    lans.append(int(input()))

#start가 0일 수가 없음
start, end = 1, max(lans)
result = 0

while start <= end:
    count = 0
    medium = (start+end)//2

    for i in range(k):
        count += lans[i]//medium

    if count >= n:
        start = medium +1
    else:
        end = medium -1
# 201
# 399
# med = 255
# end = 254
# start = 201
# 233
# end = 232
# start = 201
# 215
# end = 214
# start = 201
# 205
# end = 204
# start = 201
# 202
# end = 201
# start 201
# 201
# end = 200


#마지막에 탐색 범위가 더 이상 좁아지지 않을 떄의 end 값이 가장 긴 랜선의 길이가 되기 때문.
print(end)
