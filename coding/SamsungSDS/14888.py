import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

add, sub, mul, div = map(int, input().split())
#operator = list(map(int, input().split()))

max_result = -1e9
min_result = 1e9

def backtracking(i, arr):
    global add, sub, mul, div, max_result, min_result
    
    if i == N:
        max_result = max(max_result, arr)
        min_result = min(min_result, arr)

    else:
        if add > 0:
            add -= 1
            backtracking(i + 1, arr + A[i])
            add += 1
        if sub > 0:
            sub -= 1
            backtracking(i + 1, arr - A[i])
            sub += 1
        if mul > 0:
            mul -= 1
            backtracking(i + 1, arr * A[i])
            mul += 1
        if div > 0:
            div -= 1
            backtracking(i + 1, int(arr / A[i]))
            div += 1

backtracking(1, A[0])

print(int(max_result))
print(int(min_result))