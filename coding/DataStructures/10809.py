
import sys

input = sys.stdin.readline

alphabet = 'abcdefghijklmnopqrstuvwxyz'

S = str(input())

result = []
for i in range(len(alphabet)):
    for j in range(len(S)):
        if alphabet[i] not in S:
            result.append(-1)
            break
        if alphabet[i] == S[j]:
            result.append(j)
            break
    
for i in result:
    print(i, end=' ')