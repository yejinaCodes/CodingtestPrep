import sys
input = sys.stdin.readline

equation = list(map(str, input().split('-')))
num = []
for i in equation:
    sum_ = 0
    tmp = list(i.split('+'))
    for j in tmp:
        sum_ += int(j)
    num.append(sum_)

n = num[0]
for i in range(1, len(num)):
    n -= num[i]
print(n)