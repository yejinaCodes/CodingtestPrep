import sys
input = sys.stdin.readline

N = int(input())
nums = sorted(list(map(int, input().split())))

result = sys.maxsize
type_a, type_b, type_c = None, None, None

for _ in range(N-2):
    fixed = nums[_]
    left = _ + 1
    right = N-1

    while left < right:
        #print(left, right)
        tmp = fixed + nums[left] + nums[right]
        if abs(tmp) < abs(result):
            result = tmp
            type_a = fixed
            type_b = nums[left]
            type_c = nums[right]
        if tmp < 0:
            left += 1
        elif tmp > 0:
            right -= 1
        else:
            print(type_a, type_b, type_c)
            sys.exit()
        # elif tmp == 0:
        #     break
    # if result == 0:
    #     break

print(type_a, type_b, type_c)

    