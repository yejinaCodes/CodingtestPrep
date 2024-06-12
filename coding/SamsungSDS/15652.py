import sys
input = sys.stdin.readline

N,M = map(int,input().split())

def backtracking(answer, num, count):
    
    if count == M:
        print(*answer)
        return

    for i in range(num, N+1):
        answer.append(i)
        backtracking(answer, i, count+1)
        answer.pop()


answer = []
backtracking(answer,1,0)


