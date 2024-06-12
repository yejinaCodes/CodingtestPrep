import sys

input = sys.stdin.readline

n = int(input())
axis = []
for i in range(n):
    x,y = map(int,input().split())
    axis.append((x,y))


axis = sorted(axis, key=lambda x:(x[0], x[1]))


for i in range(n):
    print(*axis[i])