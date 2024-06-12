import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

B.sort(reverse = True)
A.sort()
result = 0
for i in range(N):
    result += B[i] * A[i]

print(result)