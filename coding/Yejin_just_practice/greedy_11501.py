import sys
input = sys.stdin.readline

T = int(input())
result = []

for testcase in range(T):
    N = int(input())
    stocks = list(map(int, input().split()))
    stocks = stocks[::-1]
    count = 0
    tmp = stocks[0]
    for i in range(1, N):
        if stocks[i] <= tmp:
            count += tmp - stocks[i]
        else:
            tmp = stocks[i]
    result.append(count)

for r in result:
    print(r)