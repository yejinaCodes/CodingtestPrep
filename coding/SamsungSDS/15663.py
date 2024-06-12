import sys
input = sys.stdin.readline

N,M = map(int,input().split())
llist = list(map(int,input().split()))
llist.sort()

check = []

#def backtracking(answer, start, prev, count):
def backtracking(answer, visited, count):

    if count == M:
        tmp = []
        for x in range(M):
            tmp.append(llist[answer[x]])
        print(*tmp)
        # tmp = []
        # for x in range(M):
        #     tmp.append(llist[answer[x]])
        
        # if len(check) == 0:
        #     check.append(tmp)
        #     return
        # elif tmp == check[-1]:
        #     return
        # else:
        #     check.append(tmp)

        return
    overlap = 0
    for i in range(N):
        #sorting되어있으니깐 마지막으로 기억하는 overlap을 확인함으로 중복된 수열을 방지함
        if not visited[i] and overlap!= llist[i]:
            visited[i] = True
            answer.append(i)
            overlap = llist[i]
            backtracking(answer, visited, count+1)
            visited[i] = False
            answer.pop()

    # for i in range(start, N):
    #     if i == prev:
    #         #print(i)
    #         continue
    #     answer.append(i)
    #     backtracking(answer, start, i, count+1)
    #     answer.pop()


answer = []
visited = [False for _ in range(N)]
backtracking(answer, visited, 0)
#backtracking(answer,0,-1,0)
# for value in check:
#    print(*value)