import sys
input = sys.stdin.readline

N,M = map(int,input().split())
llist = list(map(int,input().split()))
llist.sort()


def backtracking(answer, start, count):

    if count == M:
        tmp = []
        for x in range(M):
            tmp.append(llist[answer[x]])
        print(*tmp)
        return
    
    for i in range(start, N):
        answer.append(i)
        backtracking(answer, i+1, count+1)
        answer.pop()


answer = []
backtracking(answer, 0, 0)