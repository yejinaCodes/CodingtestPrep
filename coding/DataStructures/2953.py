#나는 요리사다
import sys
input = sys.stdin.readline

check = 0
winner = 0
for i in range(5):
    points = sum(map(int,input().split()))
    if points > check:
        check = points
        winner = i+1
print(winner, check, end=' ')
