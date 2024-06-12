import sys
input = sys.stdin.readline

N,M = map(int,input().split())
llist = list(map(int,input().split()))
llist.sort()

def backtracking(answer, start, count):

    if count == M:
        tmp = []
        for x in range(count):
            tmp.append(llist[answer[x]])
        #print(*answer)
        print(*tmp)
        return

    for i in range(start, N):
        
        if i in answer:
            continue
        
        answer.append(i)
        backtracking(answer, start, count+1)
        answer.pop()


answer = []
backtracking(answer, 0, 0)