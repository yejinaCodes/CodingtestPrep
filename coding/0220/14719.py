import sys
input = sys.stdin.readline

n,m = map(int,input().split())

block = [[0]*m for i in range(n)]

#입력값 초기화
walls = list(map(int, input().split()))
#walls 값을 block 에 1로 넣어주기
count = 0
result = 0
#walls의 작은 값 부터 확인하기 아니면 처음부터 그냥 n제곱 시간으로 탐색하기?
while True:
    if count >= m:
        break
    print(count)
    start = walls[count]
    while True:
        count = count + 1
        print('ll')
        print(count)
        if count <m and start > walls[count]:
            continue
        elif count <m and start <= walls[count]:
            for i in range(start, count):
                print('hello')
                print(i)
                print(count)
                #print(start-walls[i])
                if (start-walls[i])<0:
                    break
                result += start - walls[i]
            break
        # elif count < m and start < walls[count]:
        #     break
        elif count >= m:
            break

#print(result)


