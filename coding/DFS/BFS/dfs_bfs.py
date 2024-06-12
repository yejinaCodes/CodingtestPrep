
n,m,v = map(int, input().split())

matrix = [[0]*(n+1)for i in range(n+1)]
dfs_result = []
bfs_result = []

for _ in range(m):
    a,b = map(int,input().split())
    matrix[a][b]= 1
    matrix[b][a] = 1

visited = [0]*(n+1)


def dfs(startnode):
    visited[startnode] = 1
    dfs_result.append(startnode)

    for i in range(1, n+1):
        if visited[i] == 0 and matrix[startnode][i] == 1:
            dfs(i)

def bfs(startnode):
    queue = [startnode]
    visited[startnode] = 0

    while queue:
        startnode = queue.pop(0)
        bfs_result.append(startnode)
        for i in range(1, n+1):
            if visited[i] == 1 and matrix[startnode][i] == 1:
                queue.append(i)
                visited[i] = 0


dfs(v)
print(dfs_result)
bfs(v)
print(bfs_result)


