
#import sys
#sys.stdin = open("input.txt", "r")

def dfs(check,core2,line2):
    global core, line

    if check==s:
        if core<core2:
            core=core2
            line=line2
        elif core2==core:
            if line>line2:
                line=line2
        return

    x=cores[check][0]
    y=cores[check][1]

    for i in range(4):
        if i==0: #위
            flag=0
            for i in range(x,0,-1):
                if b[i-1][y] == 1:
                    flag=1
                    break
            if flag==1:
                continue
            else:
                for i in range(x,0,-1):
                    b[i-1][y]=1
                    line2+=1
                dfs(check+1,core2+1,line2)
                for i in range(x,0,-1):
                    b[i-1][y]=0
                    line2-=1
        elif i==1:#오른쪽
            flag=0
            for i in range(y,a-1):
                if b[x][i+1]==1:
                    flag=1
                    break
            if flag==1:
                continue
            else:
                for i in range(y,a-1):
                    b[x][i+1]=1
                    line2+=1
                dfs(check+1,core2+1,line2)
                for i in range(y,a-1):
                    b[x][i+1]=0
                    line2-=1

        elif i==2:#아래
            flag=0
            for i in range(x,a-1):
                if b[i+1][y]==1:
                    flag=1
                    break
            if flag==1:
                continue
            else:
                for i in range(x,a-1):
                    b[i+1][y]=1
                    line2+=1
                dfs(check+1,core2+1,line2)
                for i in range(x,a-1):
                    b[i+1][y]=0
                    line2-=1

        elif i==3:#왼쪽
            flag=0
            for i in range(y,0,-1):
                if b[x][i-1]==1:
                    flag=1
                    break
            if flag==1:
                continue
            else:
                for i in range(y,0,-1):
                    b[x][i-1]=1
                    line2+=1
                dfs(check+1,core2+1,line2)
                for i in range(y,0,-1):
                    b[x][i-1]=0
                    line2-=1

    dfs(check+1,core2,line2)

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    cores = []
    core = 0
    line = 0
    a = int(input())
    b = [list(map(int,input().split())) for _ in range(a)]

    #가장자리는 안 넣음
    for i in range(1, a-1):
        for j in range(1, a-1):
            if b[i][j] == 1:
                cores.append([i,j])

    s = len(cores)
    dfs(0,0,0)

    print('#{} {}'.format(test_case,line))