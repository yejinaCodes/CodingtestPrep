import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

answer = 0
# matrix= [[0]*n for i in range(n)]
matrix = [0]*n


def placable(row):
    for previousrow in range(row):
        if matrix[previousrow] == matrix[row] or abs(matrix[previousrow]-matrix[row])== abs(previousrow-row):
            return False
    #print(row, matrix[row])
    return True


#1row에 꼭 하나의 queen을 놓아야 하는 것을 사용!
def nqueen(row):
    global answer
    if row == n:
        answer += 1
    else:
        for i in range(n):
            matrix[row] = i
            if placable(row):
                print(row, matrix[row])
                nqueen(row+1)

    # possible_queens = deque()
    # # possible_queens.append((x,y))
    # x,y = row, 
    

nqueen(0)
print(answer)





    # if len(possible_queens) == n:
    #     print(possible_queens)
    #     return True
    # else:
    #     False

    # for i in range(x+1, n):
    #     for j in range(n):
    #         if j == y:
    #             break
    #         if x+1==i and y-1==j:
    #             continue
    #         elif x+1==i and y+1==j:
    #             continue
    #         else:
    #             possible_queens.append((i,j))
    # print(possible_queens)

    # for i in range(n):
    #     for j in range(n):
    #         x,y = possible_queens.popleft()
    #         if (i,j) == (x,y):
    #             continue
    #         elif i == x:
    #             continue
    #         elif j == y:
    #             continue
    #         elif x+1 == i and y-1 == j or x+1== i and y+1 == j:
    #             continue
    #         else:
    #             possible_queens.append((i,j))



#row마다 하나씩 bruteforce로 확인
# for row in range(n):
#     if nqueen(row):
#         answer+=1



# # for i in range(n):
# #     for j in range(n):
# #         if nqueen(i,j):
# #             #print(i,j)
# #             answer+=1

# print(answer)

    