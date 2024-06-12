#선을 넣을지 안넣을지 둘중 하나
#백트레킹으로 풀면 됨
#matrix로 어떻게 표현함?
#10010이런식으로?

import sys
input = sys.stdin.readline

N,M,H = map(int,input().split())
ladder_position = []
for i in range(M):
    a,b = map(int,input().split())
    ladder_position.append((a,b))

map_ = [[0]*N for _ in range(H)]
for i in ladder_position:
    a,b = i
    map_[a-1][b-1] = 1


result = []
def ladder(map):


