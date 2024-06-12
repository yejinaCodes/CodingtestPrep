import sys
input = sys.stdin.readline

def backtracking(answer, llist, visited):

    if len(answer) == 6:
        for x in range(6):
            print(llist[answer[x]], end= ' ')
        print()
        return
    
    currently_visited = visited[:]
    for i in range(len(llist)):
        if not currently_visited[i]:
            answer.append(i)
            currently_visited[i] = True
            backtracking(answer, llist, currently_visited)
            answer.pop()
            #currently_visited[i] = False

while True:
    llist = list(map(int,input().split()))

    if llist[0] == 0 and len(llist) == 1:
        #break
        sys.exit(0)
    
    #else:
    length = llist.pop(0)
    answer = []
    visited = [False] * length
    backtracking(answer, llist, visited)
    print()
        
