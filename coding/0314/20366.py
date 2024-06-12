#O(n)^3으로 풀어야 한다. 
#window를 생각해야 한다. 
#i,j 안에서 left, right pointer를 while문으로 update하지만 O(n)에 해결해야 한다. 
import sys
import itertools

N = int(input())
snowballs = list(map(int,input().split()))

#elsa가 먼저 snowball 고르고 남은 snowball중에서 anna가 2개 고르기
elsa_left = 0
for i in range(1, N):
    elsa_right = i

snowballs.sort()

'''first trial)

# import sys
# input = sys.stdin.readline

# N = int(input())
# snowballs = list(map(int,input().split()))

# #서로다른 2쌍 고르기

# snowballs.sort()

# elsa_left = 0
# elsa_right = N-1
# anna_left = 1
# anna_right = N-2

# result = 1e9

# while anna_left != anna_right:
    
#     elsa = snowballs[elsa_left] + snowballs[elsa_right]
#     anna = snowballs[anna_left] + snowballs[anna_right]

#     result = min(result, abs(elsa-anna))
#     elsa_right -= 1
#     anna_right -= 1

# print(result)
'''