import sys
input = sys.stdin.readline

N,M = map(int,input().split())

def backtracking(answer, count):

    if count == M:
        print(*answer)
        return
    
    for i in range(1, N+1):
        answer.append(i)
        backtracking(answer, count+1)
        answer.pop()
    
answer = []
backtracking(answer, 0)