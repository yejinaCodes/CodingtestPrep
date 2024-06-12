import sys

input = sys.stdin.readline

n,sum = map(int,input().split())
nums = list(map(int,input().split()))

left = 0
right = 0
answer = nums[0]

sequence = 10e9

while True:
    # if right and left == n-1:
    #     break
    if answer >= sum:
        # print('if:')
        # print(left,right)
        sequence = min(sequence, right-left+1)
        if left==n-1:
            break
        else:
            # print(answer)
            answer -= nums[left]
            left+=1
            #print(answer)
        
    else:
        # print('else:')
        # print(left,right)
        if right == n-1:
            break
        else:
            right+=1
            #print(answer)
            answer += nums[right]
            #print(answer)

if sequence == 10e9:
    print(0)
else:
    print(sequence)