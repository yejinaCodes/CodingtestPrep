import sys
input = sys.stdin.readline

level = int(input())
points = []
for i in range(level):
    points.append(int(input()))

answer = 0

points = points[::-1]

#대충 생각하지 말고!! 하나씩 차근차근히 단계별로 생각하기!! shortcut하려는 생각 버리기!!!
for i in range(level-1):
    #points[i+1] < points[i] 작을경우 생각도 해보면 좋음
    if points[i+1] >= points[i]:
        minus = points[i+1] - points[i] + 1
        points[i+1] -= minus
        answer += minus
        print(minus)

# highest = points[0]
# for i in range(1, level):
#     if points[i] >= highest - i:
#         tmp = points[i] - highest
#         answer += abs(highest-i-points[i])

    #print(answer)
print(answer)