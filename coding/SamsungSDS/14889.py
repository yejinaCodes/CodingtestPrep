import sys
import itertools
input = sys.stdin.readline

N = int(input())
S = []
for i in range(N):
    S.append(list(map(int, input().split())))

teams = [False for i in range(N)]
result = 1e9

def difference(team1, team2):
    global result
    tmp = list(itertools.permutations(team1, 2))
    tmp2 = list(itertools.permutations(team2, 2))

    group1 = 0
    group2 = 0

    for comb in tmp:
        group1 += S[comb[0]][comb[1]]
    for comb2 in tmp2:
        group2 += S[comb2[0]][comb2[1]]
    
    result = min(result, abs(group1 - group2))

def backtracking(idx, count):
    if count == N/2:
        stark = []
        link = []
        for _ in range(N):
            #true일 경우
            if teams[_]:
                stark.append(_)
            #false일 경우
            elif not teams[_]:
                link.append(_)
        difference(stark, link)
        return
    for i in range(idx, N):
        teams[i] = True
        backtracking(i+1, count + 1)
        teams[i] = False

backtracking(0, 0)

print(result)
#반복되는거는 어떻게 해결함?
    

