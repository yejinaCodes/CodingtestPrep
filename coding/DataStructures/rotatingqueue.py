import sys
#input = sys.stdin.readline #빠른 입력 함수 사용
from collections import deque
sys.stdin = open('./rotatingqueue.txt')
n, m = map(int,input().split())
pick = list(map(int,input().split()))

count = 0
#초기화하기
queue = deque([i for i in range(1,n+1)])

for p in pick:
    index = queue.index(p)
    #왼쪽으로 돌릴경우 해당 값을 첫번째 위치로 쭉 옮기고 count 해주기
    if index <= len(queue)//2:
        for i in range(index):
            x = queue.popleft()
            queue.append(x)
            count+= 1
    #오른쪽으로 돌릴경우
    else:
        #여기에서는 왜 len(queue)-index인거지?
        for i in range(len(queue)-index):
            x = queue.pop()
            queue.appendleft(x)
            count+=1
    queue.popleft()

print(count)


