import sys
input = sys.stdin.readline

N = int(input())
flowers = []
for i in range(N):
    tmp = list(map(int, input().split()))
    flowers.append([tmp[0] * 100 + tmp[1], tmp[2] * 100 + tmp[3]])

flowers.sort()
start = 301
end = 0
answer = 0

while flowers:
    #11.30까지 피는 꽃을 다 충족시켰거나 그 다음에 오는 꽃과 피는 시기가 연결되지 않을 경우 break
    if start >= 1201 or start < flowers[0][0]:
        break
    for _ in range(len(flowers)):
        if start >= flowers[0][0]:
            if end <= flowers[0][1]:
                end = flowers[0][1]
            flowers.remove(flowers[0])
        else:
            break
    start = end
    answer += 1

if start < 1201:
    print(0)
else:
    print(answer)

# def backtracking(index, start, count):
#     global end, answer
#     if start >= end:
#         answer = min(answer, count)
#         return
#     if index >= N:
#         return
#     for _ in range(index, N):
#         if flowers[_][0] <= start:
#             #flowers[_][1] >= start:
#             tmp = flowers[_][1]
#             backtracking(index+1, tmp, count+1)
    
# for i in range(N):
#     backtracking(i, start, 0)
