import sys
import heapq
from collections import deque
input = sys.stdin.readline


n,t = map(int,input().split())

rockclimbing = []
for i in range(n):
    x,y = map(int,input().split())
    rockclimbing.append((x,y))

queue = deque()

result = 0
def bfs(x,y):
    global result
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        result +=1
        for i in range(n):
            a,b = rockclimbing[i]
            if abs(a-x)<=2 and abs(b-y)<=2:
                queue.append((a,b))
            

bfs(0,0)
print(result)