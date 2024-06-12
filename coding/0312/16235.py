import sys
from copy import deepcopy
input = sys.stdin.readline
N,M,K = map(int,input().split())

#매년 위치별로 영양분 matrix
adding_nutrition = []
for i in range(N):
    line = list(map(int,input().split()))
    adding_nutrition.append(line)

nutrition = deepcopy(adding_nutrition)
for i in range(N):
    for j in range(N):
        nutrition[i][j] += 5

#i,j 위치에 나무의 나이 저장하는 tree matrix
tree = [[]for i in range(N)]
for i in range(N):
    for j in range(N):
        tree[i].append([])

#초기화
for y in range(M):
    i,j, age = map(int,input().split())
    tree[i-1][j-1].append(age)

dead_trees = []
#k년수까지 나무 재태크
while K:
    kth_tree_num = 0
    #봄
    for i in range(N):
        for j in range(N):
            tree[i][j].sort()
            tmp = []
            for age in tree[i][j]:
                if nutrition[i][j] < age:
                    dead_trees.append([i,j,age])
                    continue
                nutrition[i][j] -= age
                tmp.append(age+1)
            tree[i][j] = tmp
            tree[i][j].sort()
    #여름
    if len(dead_trees) > 0:
        for dead in dead_trees:
            addition = dead[2]//2
            nutrition[dead[0]][dead[1]] = addition

    #tuple형식으로 하면 어떻게 됨?
    direction = [[-1,-1], [-1,0], [-1,1], [0,-1], [0,1], [1,-1], [1,0], [1,1]]

    #가을
    for i in range(N):
        for j in range(N):
            for age in tree[i][j]:
                if age%5 == 0:
                    for dir in direction:
                        nx = i + dir[0]
                        ny = j + dir[1]
                        if 0<=nx<N and 0<=ny<N:
                            tree[nx][ny].append(1)
    #겨울
    for i in range(N):
        for j in range(N):
            cal_tree = len(tree[i][j])
            kth_tree_num += cal_tree
            nutrition[i][j] += adding_nutrition[i][j]
    print(nutrition)

    K = K-1


print(kth_tree_num)