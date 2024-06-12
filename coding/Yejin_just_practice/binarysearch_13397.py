import sys
input = sys.stdin.readline

N,M = map(int,input().split())
array = list(map(int,input().split()))

#이진탐색으로 얻은 값이 M개의 구간을 만들 수 있는지 확인하는 코드임.
start = 0
end = max(array)
result = 0

def check_mid(mid):
    #구간3개에 2개의 칸?이 존재하기 때문
    count = 1
    #2pointer을 사용
    minval = array[0]
    maxval = array[0]
    print(mid)
    for i in range(1, N):
        minval = min(minval, array[i])
        maxval = max(maxval, array[i])
        print(maxval,minval)
        if maxval - minval > mid:
            count += 1
            #print(maxval, minval)
            print('check')
            print(count)
            maxval = array[i]
            minval = array[i]
    return count

while start <= end:
    mid = (start+end)//2
    if check_mid(mid) <= M:
        #구간의 개수를 늘려야 하기 때문에 mid 값이 작아져야 한다.
        result = mid
        end = mid-1
    else:
        start = mid+1


print(result)