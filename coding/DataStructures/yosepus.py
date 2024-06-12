import sys
input = sys.stdin.readline
from collections import deque

n,k = map(int,input().split())
circle = deque([i for i in range(1, n+1)])

result = []
while circle:
    for i in range(k-1):
        x = circle.popleft()
        circle.append(x)
    result.append(circle.popleft())

print('<', end='')
for i in range(len(result)):
    if i < len(result)-1:
        print(result[i], end=', ')
    else:
        print(result[i], end='')
print('>')

#print('<', *result, sep=',', '>')
