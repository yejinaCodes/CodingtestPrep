import sys
input = sys.stdin.readline

N, K = map(int, input().split())

coins = []
for i in range(N):
    coins.append(int(input()))

coins.sort(reverse = True)
result = 0

while K > 0:
    for i in range(N):
        if (K // coins[i]) < 0:
            continue
        else:
            tmp = K//coins[i]
            K -= tmp * coins[i]
            result += tmp
            #print(tmp)

print(result)