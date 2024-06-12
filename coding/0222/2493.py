import sys
input = sys.stdin.readline
#left right pointer사용하기

N = int(input())
tops = list(map(int,input().split()))

answer = []
answer.append(0)
leftpointer = 0

#왼쪽 -> 오른쪽으로 체크. 숫자가 커지거나 작아지는거에 따라 다른 값 저장
for i in range(N):
    if tops[i] > tops[leftpointer]:
        #print(i, leftpointer)
        answer.append(answer[-1])
        leftpointer = i
    elif tops[i] < tops[leftpointer]:
        answer.append(leftpointer+1)
        leftpointer = i

print(*answer)