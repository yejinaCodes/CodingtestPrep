import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int,input().split())

fishbowl = [deque(map(int,input().split()))]
#print(fishbowl)
magic = 0

def update_minfish(fishbowl):
    min_fish = min(fishbowl[0])
    for i in range(N):
        if fishbowl[0][i] == min_fish:
            fishbowl[0][i] += 1

def remove_emptylist(fishbowl):
    new_fishbowl = []
    for i in range(len(fishbowl)):
        if len(fishbowl[i]) == 0:
            continue
        else:
            new_fishbowl.append(fishbowl[i])
    
    return new_fishbowl


def rotate90(fishbowl):
    #공중 어항의 오른쪽 어항 바닥보다 크면 break
    float_len = len(fishbowl[-1])
    right_len = len(fishbowl[0]) - float_len
    while float_len <= right_len:
        #print(fishbowl)
        #공중 부양 칸 고르기
        float_tmp = []
        for i in range(len(fishbowl)):
            tmp = []
            for j in range(float_len):
                x = fishbowl[i].popleft()
                tmp.append(x)
            float_tmp.append(tmp)

        #print(float_tmp)
        
        fishbowl = remove_emptylist(fishbowl)
        print(fishbowl)
        #90rotate하기
        #위에서부터, 뒤에서부터 뽑기
        rotate_tmp = []
        #for i in range()
        while float_tmp:
            #print(float_tmp)
            rtmp = []
            #deque은 index으로 접근하기!
            for j in range(len(float_tmp)):
                if len(float_tmp[j]) == 0:
                    del float_tmp[j]
                    break
                x = float_tmp[j].pop()
                rtmp.append(x)
            if rtmp:
                rotate_tmp.append(rtmp)  
        
        #print(rotate_tmp)

        #오른쪽 어항에 append하기
        #print(fishbowl)

    

while max(fishbowl[0]) - min(fishbowl[0]) > K:

    update_minfish(fishbowl)
    #미리 하나 뽑아서 쌓아 놓기
    first = [fishbowl[0].popleft()]
    fishbowl.append(deque(first))
    #90회전
    rotate90(fishbowl)


print(magic)