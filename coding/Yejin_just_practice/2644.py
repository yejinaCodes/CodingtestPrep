#adjacency list 사용하기
#dfs로 풀기

import sys
input = sys.stdin.readline

N = int(input())
findx, findy = map(int, input().split())
n = int(input())
#adjacency_list = {i: [] for i in range(1, N+1)}
adjacency_matrix = [[] for _ in range(N+1)]
visited = [False] * (N+1)
result = []

#2차원 배열에 저장
for _ in range(n):
    x, y = map(int, input().split())
    adjacency_matrix[x].append(y)
    adjacency_matrix[y].append(x)

#dfs
def dfs(v, num):
    if v == findy:
        result.append(num)
    num += 1
    visited[v] = True
    # if v == findy:
    #     result.append(num)
    for i in adjacency_matrix[v]:
        if not visited[i]:
            dfs(i, num)


dfs(findx, 0)
if len(result) == 0:
    print(-1)
else:
    print(result[0])