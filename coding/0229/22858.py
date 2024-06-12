import sys
import copy
input = sys.stdin.readline


n, k = map(int, input().split())

result = list(map(int, input().split()))
order = list(map(int,input().split()))

# reverse_order = []
# for i in range(n):
#     reverse_order.append(0)

# for i in range(n):
#     reverse_order[order[i]-1] = i+1

tmp = [0 for i in range(n)]

for _ in range(k):
    for i in range(n):
        tmp[order[i]-1]= result[i]

    result = copy.deepcopy(tmp)
    
print(*tmp)

# while k>0:
    
#     for i in range(n):
#         tmp[reverse_order[i]-1] = result[i]

#     result = copy.deepcopy(tmp)

#     k-=1

