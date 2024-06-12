import sys
input = sys.stdin.readline

N = int(input())
atms = list(map(int, input().split()))

atms.sort()
answer = [atms[0]]

for i in range(1, N):
    tmp = answer[i-1] + atms[i]
    #print(tmp)
    answer.append(tmp)

print(sum(answer))