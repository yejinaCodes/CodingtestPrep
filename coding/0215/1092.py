# #maxheap으로 풀면 될 것 같음

# ##nono 최적의 해를 구하는 방법으로 가야하는 것 같음. 주현님 코드 참고. 그리디로 풀기. 
# ##최대한 분배가 잘 되는게 박스를 옮기는 최솟값이다.
# ##min으로 정렬한다음에 각 weights boxs가 
# ##
# import sys
# import heapq

# input = sys.stdin.readline

# crane = int(input())
# weights_c= list(map(int,input().split()))
# weights_c.sort(reverse=True)


# box = int(input())
# weights_b = list(map(int,input().split()))
# weights_boxes = []
# for i in range(box):
#     heapq.heappush(weights_boxes, -weights_b[i])

# count = 0
# flag = False
# if weights_c[0] < weights_boxes[0]:
#     print(-1)
#     sys.exit()

# while len(weights_boxes)>0:
#     for i in range(crane):
#         num = -heapq.heappop(weights_boxes)
#         if weights_c[i] < num:
#             heapq.heappush(weights_boxes, -num)
#         if len(weights_boxes) == 0:
#             flag = True
#             break
#     if not flag:
#         count +=1
#     else:
#         break


# print(count)

#주현님 코드
import sys

def input():
    return sys.stdin.readline()

N = int(input())
max_weight = list(map(int, input().split()))
M = int(input())
box_weight = list(map(int, input().split()))

def solution():
    carry = [0] * N
    max_weight.sort()
    box_weight.sort()

    if max_weight[-1] < box_weight[-1]:
        return -1

    sb = 0
    for i, c in enumerate(max_weight):
        left_box = len(box_weight[sb:])
        left_craine = N - i

        if left_box % left_craine == 0:
            max_carry = int(left_box // left_craine)
        else:
            max_carry = int(left_box // left_craine) + 1

        count = 0
        for j in range(sb, M):
            if c < box_weight[j]:
                carry[i] = count
                break

            if count == max_carry:
                carry[i] = max_carry
                break

            if j == M-1:
                carry[i] = count+1
                break

            count += 1

        sb += count

    return max(carry)

print(solution())