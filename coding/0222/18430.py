import sys
input = sys.stdin.readline

def dfs(i,j,sum):
    global answer
    if j==m:
        i+=1
        j=0
    #다른 것은 확인할 필요가 없나? 없다. 이미 위에서 j==m으로 처리됨. n일경우 이미 모든 칸을 확인했음.
    #끝까지 다 탐색을 다 했을 경우:
    if i==n:
        answer = max(answer, sum)
        return

    if not visited[i][j]:
        #가능한 shape찾기
        #여기서 그다음으로 어떻게 넘어감. 한칸에 대해서 4개 shap 다 체크한다음에...
        for s in range(4):
            a,b,c,d = shape_dict[s]
            x,y,xx,yy = a+i,b+j,c+i,d+j
            if x>=0 and x<n and xx>= 0 and xx< n and y>=0 and y<m and yy>=0 and yy<m and not visited[x][y] and not visited[xx][yy]:
                visited[i][j] = True
                visited[x][y] = True
                visited[xx][yy] = True
                dfs(i,j + 1,sum + wood[i][j]*2 + wood[x][y] + wood[xx][yy])
                visited[i][j] = False
                visited[x][y] = False
                visited[xx][yy] = False
    dfs(i,j+1,sum)

n,m = map(int,input().split())
wood = [list(map(int,input().split())) for i in range(n)]
#i,j에서 양쪽 wing 방향 계산을 위한 값들 정리해 놓기
shape_dict = {0:[0,-1,1,0], 1:[-1,0,0,-1], 2:[-1,0,0,1], 3:[0,1,1,0]}

#visited확인을 위해 list 사용하기
visited = [[False]*m for _ in range(n)]

answer = 0
dfs(0,0,0)
print(answer)


# import sys
# input = sys.stdin.readline

# n, m = map(int,input().split())
# material = []
# for i in range(n):
#     material.append(list(map(int,input().split())))

# if n < 2:
#     print(0)
#     sys.exit()

# #높은 중간값 순서로 부메랑 만들수 있는지 location으로 확인해보기

# location = []
# #i,j for each number
# for i in range(n):
#     for j in range(n):
#         location[i].append(j)

#내림순으로 정렬된 스텍 사용하기?
        


#최대 몇개의 부메랑을 만들 수 있느지를 체크하고 진행하기?
#3x2 = 2개, 3x3 = 2개, 4x2 = 2개, 4x3 = 4개

# for i in range(n):
#     print(location[i])

# def boomerang(x,y):
    

