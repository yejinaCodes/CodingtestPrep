import sys
input = sys.stdin.readline
from copy import deepcopy

N = int(input())
students_every_class = list(map(int,input().split()))

B,C = map(int,input().split())

total_watcher = 0
for classroom in students_every_class:
    #꼭 총괄을 한번 써야함. 딱 한번!
    classroom -= B
    total_watcher += 1
    if classroom > 0 and classroom%C == 0:
        #print(total_watcher)
        total_watcher += (classroom//C)
    elif classroom > 0 and classroom%C != 0:
        total_watcher += (classroom//C) + 1
        #print(total_watcher)

print(total_watcher)