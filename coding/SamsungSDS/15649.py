import sys
input = sys.stdin.readline


def backtracking(answer, check, checklist):

    if check>=M:
        print(*answer)
        #print(''.join(str(answer)))       
        return
    
    for i in range(1, N+1):
        if checklist[i]:
            #print('hmm')
            continue
        else:
            checklist[i] = True
            answer.append(i)
            #print(answer)
            backtracking(answer, check+1, checklist)
            #print('ch')
            checklist[i] = False
            answer.pop()

N,M = map(int,input().split())
answer = []
checklist = [False for _ in range(N+1)]
backtracking(answer, 0, checklist)
