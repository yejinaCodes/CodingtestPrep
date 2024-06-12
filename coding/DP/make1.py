#1463
#greedy방식으로 생각하면 안됨.

n = int(input())

dp = [0]* (n+1)
for i in range(2, n+1):
    