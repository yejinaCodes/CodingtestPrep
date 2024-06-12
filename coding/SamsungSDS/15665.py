import sys
input = sys.stdin.readline

N,M = map(int,input().split())
llist = list(map(int,input().split()))
llist.sort()

def backtracking(answer, count):
    if count == M:
        tmp = []
        for x in range(M):
            tmp.append(llist[answer[x]])
        print(*tmp)
        return

    overlap = 0
    for i in range(N):
        if overlap != llist[i]:
            answer.append(i)
            overlap = llist[i]
            backtracking(answer, count+1)
            answer.pop()

answer = []
backtracking(answer, 0)