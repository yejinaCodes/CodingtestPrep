import sys
input = sys.stdin.readline

N,S = map(int,input().split())

llist = list(map(int,input().split()))
answer = []
count = 0 
def backtracking(start):
    global count
    if len(answer) > 0 and sum(answer) == S:
        count += 1
        #여기서 return을 해주면 안됨!! 왜냐!! 뒤에 -5,5가 나오면 다시 S를 얻을 수 있기 때문!
        #return 
    
    for i in range(start, N):
        answer.append(llist[i])
        backtracking(i+1)
        #알아서 return 되는 건가?
        answer.pop()


start = 0
backtracking(start)
print(count)



# import sys
# input = sys.stdin.readline

# N,S = map(int,input().split())

# llist = list(map(int,input().split()))

# count = 0

# def backtracking(answer, index):
#     global count

#     if index >= N:
#         return
    
#     answer += llist[index]
#     if answer == S:
#         count +=1
    
#     backtracking(answer, index+1)
#     backtracking(answer-llist[index], index+1) #넣은거 다시 빼주기

# backtracking(0,0)
# print(count)


# import sys
# input = sys.stdin.readline

# N,S = map(int,input().split())

# llist = list(map(int,input().split()))

# result = 0 
# def backtracking(answer, start):
#     global result
#     if len(answer) > 0 and sum(answer) == S:
#         result += 1
#         return 
    
#     for i in range(start, N):
#         answer.append(llist[i])
#         print('append:', llist[i])
#         print(answer)
#         backtracking(answer, i+1)
#         answer.pop()


# answer = []
# start = 0
# backtracking(answer, start)

# print(result)






# import sys
# input = sys.stdin.readline

# N, S = map(int,input().split())

# llist = list(map(int,input().split()))

# def backtracking(answer, visited, llist):

#     if answer == S:
#         print(answer)
#         return 


#     currently_visited = visited[:]
#     for i in range(1, N):

#         if not currently_visited[i]:
#             answer += llist[i]
#             #print(answer)
#             currently_visited[i] = True
#             backtracking(answer, currently_visited, llist)




# answer = llist[0]
# visited = [False]*N
# backtracking(answer, visited, llist)


