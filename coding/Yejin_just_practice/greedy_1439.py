#import sys
#input = sys.stdin.readline

S = str(input())
#grouping 개수 찾기

count = 0
for i in range(len(S)-1):
    if S[i] != S[i+1]:
        count += 1

print((count +1)//2)

#입력 받은 string -> 변화 횟수 -> 뒤집어야할 횟수
'''
0 -> 0 -> 0
01 -> 1 -> 1
010 -> 2 -> 1
0101 -> 3 -> 2
01010 -> 4 -> 2
010101 -> 5 -> 3
'''
#그래서 count+1 을 해줘야 함