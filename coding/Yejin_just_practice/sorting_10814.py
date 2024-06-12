import sys
input = sys.stdin.readline


n = int(input())
llist = []
for i in range(n):
    v, m = map(str,input().split())
    llist.append((int(v),m))

llist = sorted(llist, key=lambda x:x[0])
for i in range(n):
    print(*llist[i])