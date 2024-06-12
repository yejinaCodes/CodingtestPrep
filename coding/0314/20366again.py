#sliding window + 투 포인터를 사용해야 함

#고정 사이즈의 원도우가 이동하면서 윈도우 내에 있는 데이터를 이용해 문제를 풀이하는 알고리즘을 뜻함

#투 포인터는 구간의 넓이가 조건에 따라 유동적으로 변하며, 슬라이딩 윈도우 알고리즘은 항상
#구간의 넓이가 고정되어 있다는 차이점이 있다.

import sys
input = sys.stdin.readline

n = int(input())
snowballs = list(map(int,input().split()))
snowballs.sort()

answer = 1e9

for i in range(n):
    leftpointer = i+1
    for j in range(i+3, n):
        rightpointer = j-1

        while leftpointer < rightpointer:
            elsa = snowballs[i] + snowballs[j]
            anna = snowballs[leftpointer] + snowballs[rightpointer]
            difference = elsa-anna
            #안에서 투포인터 써야하기 때문에 조건 정하기
            if abs(difference) < answer:
                answer = abs(difference)

            #anna 크기 조절하기..
            #anna가 elsa보다 클 경우, anna의 크기를 줄여야함.
            if difference < 0:
                rightpointer -= 1
            #anna가 elsa보다 작을 경우, anna크기를 늘려야 함. 
            elif difference > 0:
                leftpointer += 1
            else:
                print(0)
                sys.exit()



print(answer)