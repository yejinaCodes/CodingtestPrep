import sys
input = sys.stdin.readline

N, M = map(int,input().split())

def backtracking(answer,start, count):

    if count == M:
        print(*answer)
        return 

    for i in range(start, N+1):
        answer.append(i)
        backtracking(answer, i+1, count+1)
        answer.pop()


answer = []
backtracking(answer, 1, 0)
