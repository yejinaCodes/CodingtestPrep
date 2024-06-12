#n < 3,000,000
from collections import defaultdict
n,d,k,c = map(int, input().split())
sushi_list = []

for _ in range(n):
    sushi_list.append(int(input()))

sushi_list.extend(sushi_list)
d = defaultdict(int)
right,left = 0,0

while right < k:
    d[sushi_list[right]] += 1
    right += 1

d[c] += 1
answer = 0
while right < len(sushi_list):
    answer = max(answer, len(d))
    #print('answer:', answer)
    #print(d)

    d[sushi_list[left]] -= 1
    if d[sushi_list[left]] == 0:
        del d[sushi_list[left]]
    
    d[sushi_list[right]] += 1
    left += 1
    right += 1

print(answer)



# import sys
# from collections import deque
# input = sys.stdin.readline

# sushi_comb_max = 0
# N, d, k, c = map(int, input().split())
# sushi_list = []
# for _ in range(N):
#     sushi_list.append(int(input()))

# #2 for loop 사용하면 안됨. sliding window로 시간초과 해결해야 함.
# que  = deque(sushi_list[:k])
# for i in range(N):
#     if i != 0:
#         if i <= N//2:
#             que.append(sushi_list[i+k+1])
#         else:
#             que.append(sushi_list[k-(N-i)-1])
#     tmp = set(que)
#     tmp.add(c)
#     sushi_comb_max = max(sushi_comb_max, len(tmp))
#     que.popleft()

# print(sushi_comb_max)