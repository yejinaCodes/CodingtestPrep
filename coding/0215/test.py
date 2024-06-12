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