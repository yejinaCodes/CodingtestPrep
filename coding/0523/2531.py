#n < 30,000
import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
sushi_list = []
for _ in range(n):
    sushi_list.append(int(input()))

answer = 0
for i in range(n):
    if i <= n-k:
        tmp = set(sushi_list[i:i+k])
    else:
        tmp = set(sushi_list[i:])
        tmp.update(sushi_list[:(i+k)%n])
    
    tmp.add(c)
    answer = max(answer, len(tmp))

print(answer)