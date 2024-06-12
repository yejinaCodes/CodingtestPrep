import sys
input = sys.stdin.readline
N, K = map(int,input().split())
fishbowl = [list(map(int,input().split()))]

result = 0
def init(n):
    min_fish = min(n[0])
    for i in range(len(n[0])):
        if n[0][i] == min_fish:
            #print(n[i])
            n[0][i] += 1

    first = n[0].pop(0)
    n.append([first])
    return n

def delete_emptylist(n):
    new_n = []
    for i in range(len(n)):
        if len(n[i]) == 0:
            continue
        else:
            new_n.append(n[i])

    return n


    # for l in range(len(n)):
    #     if len(n[l]) == 0:
    #         n.pop(l)
    # return n

def rotate90(n):
    final = []
    #len(n[-1]
    while True:
        if len(n) > (len(n[0]) - len(n[-1])):
            break
        #print(len(n))
        #print(len(n[0])-len(n))
        tmp_box = []
        for i in range(len(n[-1])):
            tmp = []
            for j in range(len(n)):
                tmp.append(n[j].pop(0))
            tmp_box.append(tmp)
        n = delete_emptylist(n)
        for i in range(len(tmp_box)-1,-1,-1):
            n.append(tmp_box[i])
    return n
    #     for j in range(len(n[-1])-1, -1, - 1):
    #         #print(j)
    #         tmp = []
    #         for i in range(len(n)):
    #             x = n[i].pop(j)
    #             tmp.append(x)
    #         #tmp_box.append(tmp)
    #         if len(tmp) == len(n):
    #             tmp_box.append(tmp)
    #
    #     n = delete_emptylist(n)
    #     #print(n)
    #     for x in tmp_box:
    #         n.append(x)
    #     #print(n)
    #     final = n
    # #print(final)
    # return final

def rotate180(n):
    num = len(n)//2
    tmp = []
    second_tmp = []
    for i in range(num-1, -1,-1):
        x = n.pop(i)
        tmp.append(x)

    second_tmp.append(n)
    second_tmp.append(tmp)
    #print(second_tmp)

    #두번째
    snum = len(second_tmp[0])//2
    ttmp = []
    for i in range(len(second_tmp)-1, -1, -1):
        tmp = []
        for j in range(snum-1,-1,-1):
            x = second_tmp[i].pop(j)
            tmp.append(x)
        #print(tmp)
        ttmp.append(tmp)

    for i in range(len(ttmp)):
        second_tmp.append(ttmp[i])

    n = second_tmp
    return n

def manipulate_num(n):
    dx = [-1,1,0,0] #상하좌우
    dy = [0,0,-1,1]

    tmp = [[0]*N for _ in range(N)]
    for_cal = [[0]*N for _ in range(N)]
    visited = [[False]*N for _ in range(N)]

    # for i in range(len(n)):
    #     tmp.append([0 for _ in range(len(n[i]))])
    for i in range(len(n)):
        for j in range(len(n[i])):
            tmp[i][j] = n[i][j] #그 외에 값들은 다 0임. simple하게 생각하기!!!

    #print(tmp)

    for i in range(N):
        for j in range(N):
            x, y = i,j
            visited[x][y] = True

            if tmp[x][y] == 0:
                continue

            for d in range(4):
                nx = dx[d] + x
                ny = dy[d] + y
                #list out of range 나옴...
                if nx <0 or nx >= N or ny <0 or ny >= N or tmp[nx][ny]== 0 or visited[nx][ny]:
                    continue

                prev = tmp[x][y]
                new = tmp[nx][ny]
                d = abs(prev - new) // 5
                if d > 0:
                    if prev > new:
                        for_cal[x][y] -= d
                        for_cal[nx][ny] += d
                    elif new > prev:
                        for_cal[x][y] += d
                        for_cal[nx][ny] -= d

    for i in range(N):
        for j in range(N):
            if for_cal[i][j] == 0:
                continue
            else:
                n[i][j] += for_cal[i][j]

    return

def linearify(n):
    add = []
    #2개 이상인 어항 뽑기
    for i in range(len(n[-1])):
        tmp = []
        for j in range(len(n)):
            tmp.append(n[j].pop(0))
        add.append(tmp)
        n = delete_emptylist(n)

    #바닥에 남은 어항 뽑기
    if len(n) > 0:
        add.append([i for i in n[0]])
    line = []
    for i in range(len(add)):
        line.extend(add[i])

    return line


    # tmp = [[0]*(len(n[0])) for _ in range(len(n))]
    # linear = []
    # for i in range(len(n)):
    #     for j in range(len(n[i])):
    #         tmp[i][j] = n[i][j]
    #
    # for j in range(len(n[0])):
    #     for i in range(len(n)):
    #         if tmp[i][j] == 0:
    #             continue
    #         else:
    #             linear.append(tmp[i][j])
    # return linear

while True:
    fishbowl = init(fishbowl)
    # print(fishbowl)

    fishbowl = rotate90(fishbowl)

    manipulate_num(fishbowl)

    fishbowl = linearify(fishbowl)

    fishbowl = rotate180(fishbowl)

    manipulate_num(fishbowl)

    fishbowl = linearify(fishbowl)

    result += 1

    if max(fishbowl[0]) - min(fishbowl[0]) > K:
        break
    print(result)

#print(result)