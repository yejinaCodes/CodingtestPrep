import sys

input = sys.stdin.readline

#graph 순회
N = int(input())

nodes_list = []

for i in range(N):
    a, b, c = map(int, input().split())
    if a == 1:
        nodes_list.append(0)
        nodes_list.append(a)
        nodes_list.append(b)
        nodes_list.append(c)
    else:
        nodes_list.append(b)
        nodes_list.append(c)

#앞에 칸은 비우고 index를 1부터 카운트하기
visited = [False for i in range(N*2+2)]

count = 0
pointer = 1

#재귀적으로 풀어야 할 것 같음.
def check_leftchild(index):
    if nodes_list[index*2] < 0:
        visited[index*2] = True
        return False
    elif nodes_list[index*2] > 0 and visited[index*2] == False:
        return True

def check_rightchild(index):
    if nodes_list[index*2+1] < 0:
        visited[index*2+1] = True
        return False
    elif nodes_list[index*2+1] > 0 and visited[index*2+1] == False:
        return True


while visited[N] == False:
    if pointer == N:
        break

    if check_leftchild(pointer):
        #and visited[pointer]== False
        visited[pointer] = True
        pointer = pointer*2
        count += 1
    elif check_rightchild(pointer):
        #and visited[pointer] == False
        visited[pointer] = True
        pointer = pointer*2+1
        count += 1
    else:
        pointer = pointer//2
        count += 1


print(count)




# def check_leftchild(index):
#     #index = index*2
#     if nodes_list[index*2] < 0:
#         visited[index*2] = True
#         return index
#     elif nodes_list[index*2] > 0:
#         count[0] += 1
#         visited[index*2] = True
#         return check_leftchild(index*2)

# def check_rightchild(index):
#     if nodes_list[index*2+1] < 0:
#         visited[index*2+1] = True
#         return index
#     elif nodes_list[index*2+1] > 0:
#         count[0] += 1
#         visited[index*2+1] = True
#         return index*2+1
        




# while visited[-1] == False:

#     #자식 확인하기
#     if nodes_list[pointer] > 0 and visited[pointer] == False:
#         visited[pointer] = True
#         pointer += pointer
#         count += 1
#     #부모로 다시 올라가기
#     elif nodes_list[pointer] < 0 and visited[pointer] == False:
#         visited[pointer] = True
#         pointer = pointer//2
#         count += 1
    
        



