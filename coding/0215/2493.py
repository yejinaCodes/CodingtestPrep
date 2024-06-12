#자료구조 stack을 활용해야 함
import sys
input = sys.stdin.readline

n = int(input())
tops = list(map(int,input().split()))

stack = []
#default로 0을 세팅해주는 것이 좋음. 
answer = [0 for i in range(n)]

for i in range(n):
    #수신 가능한 것만 남기고 아닌 것은 pop해줘야 함.
    while stack:
        if stack[-1][1] > tops[i]:
            #수신 가능이기 때문에 저장한다.
            answer[i] = stack[-1][0] + 1
            #만약에 stack에 있는값이 크면 break해서 tops[i] 값도 stack에 넣어줘야 함.
            break
        else:
            #수신 불가능이기 때문에 pop한다.
            stack.pop()
    
    stack.append([i,tops[i]])

print(*answer)








# #9가 못하는 이유: 낮은 곳-> 높은 곳으로 수신 가능

# import sys
# input = sys.stdin.readline

# tower = int(input())

# heights = list(map(int,input().split()))

# process = []
# result = []
# #stack사용

# # process.append((1, heights[0]))
# # result.append(0)

# # while process:
# #     #check
# #     for i in range(1, tower):
# #         if process[-1][1] >= heights[i]:
# #             result.append(process[-1][0]+1)
# #             #process.pop()
# #             process.append((i+1, heights[i]))
# #         else:
# #             process.pop()
# #             result.append(0)
# #             process.append((i+1, heights[i]))
# #             #index, receiving_tower = process.pop()
# #         #result.append()


# # print(result)

# for i in range(tower):
#     while process:
#         if process[-1][1] >= heights[i]:
#             #여기에서 pop을 하면 안됨. 왜냐하면..
#             result.append(process[-1][0]+1)
#             #process.append((i+1,heights[i]))
#             break
#         else:
#             #그 다음 답이 더 클 경우, 수신이 가능하지 않다. 어차피 왼쪽으로 밖에 수신을 하기 때문에
#             #다음 다음에 나오는 탑에 경우에도 해당 탑은 선택 될 수 없다.
#             process.pop()
#             #process.append((i+1,heights[i]))
#     if not process:
#         result.append(0)
#     process.append((i,heights[i]))

# print(result)