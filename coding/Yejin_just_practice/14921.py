import sys
input = sys.stdin.readline

N = int(input())
nums = sorted(list(map(int, input().split())))

#answer = 1e9


left = 0
right = N-1
answer = nums[left] + nums[right]
while left < right:
    tmp = nums[left] + nums[right]
    if abs(answer) > abs(tmp):
        #absolute값이 answer이 되면 안됨!
        answer = tmp
    if tmp >= 0:
        right -= 1
        #answer = min(abs(answer), abs(tmp))
    elif tmp < 0:
        left += 1
        #answer = min(abs(answer), abs(tmp))
    #else:
    #    print(0)
    #    sys.exit()
print(answer)
