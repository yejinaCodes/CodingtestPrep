#사이클 게임

#union find 사용

#최악의 경우를 고려해 path compression 사용하기
#3개의 점이 같은 부모 노드 root를 가르키면 cycle 완성

import sys

input = sys.stdin.readline

n,m = map(int,input().split())

#root check용
root = [0] * n
#root 초기화
for i in range(n):
    root[i] = i

#두 원소가 속한 집합을 합치기
def union(root, num1,num2):
    x = find_parent(root, num1)
    y = find_parent(root,num2)

    if x < y:
        root[y] = x
    else:
        root[x] = y


#부모 노드가 같은지 확인하기
def find_parent(root, num):
    if root[num] != num:
        root[num] = find_parent(root, root[num])
    return root[num]

#count = 0
cycle = False

for i in range(m):
    x,y = map(int,input().split())

    if find_parent(root, x) == find_parent(root, y):
        cycle = True
        print(i+1)
        break
    else:
        union(root, x, y)

if not cycle:
    print(0)