import sys
input = sys.stdin.readline

def union(root, num1, num2):
    x = find_root(root, num1)
    y = find_root(root, num2)
    if x < y:
        root_num = find_root(root, root[num2])
        root[root_num] = x
    else:
        root_num = find_root(root, root[num1])
        root[root_num] = y

def find_root(root, num):
    if root[num] != num:
        root[num] = find_root(root, root[num])
    return root[num]

n,m = map(int,input().split())
root = [0]* (n+1)
#초기화
for i in range(1, n+1):
    root[i] = i

for i in range(m):
    x,y= map(int,input().split())
    union(root, x,y)

#고유한 집합의 수를 찾으면 됨...
counter = set()
for i in range(1, n+1):
    counter.add(find_root(root, i))
    # print(find_root(root, i))

#print(root)
    
print(len(counter))

# if len(counter) == n:
#     print(0)
# else:
#     print(len(counter))