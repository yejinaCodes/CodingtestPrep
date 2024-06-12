import sys
input = sys.stdin.readline

N,K = map(int,input().split())
fishbowl = list(map(int,input().split()))

def stackbowl(fishbowl):
    #tmp = [0 for _ in range(N-1)]
    tmp = []
    process_fishbowl = []
    tmp.append(fishbowl[0]) 
    #= fishbowl[0]
    fishbowl = fishbowl[1:]
    process_fishbowl.append(tmp)
    process_fishbowl.append(fishbowl)
    return process_fishbowl
    
def rotate90stack(process_fishbowl, step):

    #부양할 값들 tmp에 저장
    tmp = []
    ln = len(process_fishbowl[0])
    tmp.append(process_fishbowl[0])

    #이 부분을 쉽고 빠르게 바꿀 수 있는 방법..
    for i in range(1, len(process_fishbowl)):
        if i == len(process_fishbowl)-1:
            #ln 만큼만 tmp에 append 해주기 
            pass
            
        tmp.append(process_fishbowl[i])

    #90도 회전

    #오른쪽 어항의 바닥이 더 작을 경우 return False

    #오른쪽에 있는 어항의 바닥에 쌓기


def adjustfish(process_fishbowl):
    pass

def linearstack(process_fishbowl):
    pass

def rotate180stack(process_fishbowl):

    pass

while (max(fishbowl) - min(fishbowl)) > K:

    #1. 적은 어항 +1 
    minfish = min(fishbowl)
    for i in range(N):
        if fishbowl[i] == minfish:
            fishbowl[i] = minfish + 1
    #2. 어항 쌓기
    process_fishbowl = stackbowl(fishbowl)
    step = 0

    #3. 전체 회전 + 바닥에 있는 어항 위에 쌓기 
    while True:
        step += 1
        process_fishbowl2 = rotate90stack(process_fishbowl, step)
    
    #4. 물고기 수 조절
    adjustfish(process_fishbowl2)
    
    #5. 일렬로 놓기
    linearstack(process_fishbowl2)

    #6. 공중부양 180도 회전 + 바닥에 있는 N/2개 어항 위에 쌓기
    rotate180stack(process_fishbowl2)

    #7. 물고기 수 조절
    adjustfish(process_fishbowl2)

    #8. 일렬로 놓기
    linearstack(process_fishbowl2)

    

