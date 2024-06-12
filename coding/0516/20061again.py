
def blue_insert(t, x):
    c_idx = 0
    r = x
    if t == 1:
        #왜 6까지가 아니지?
        while blue[r][c_idx] == 0 and c_idx < 5: #c_idx가 최대 4까지 가능해야함
            c_idx += 1
        if blue[r][c_idx] == 1:
            c_idx -= 1
    elif t == 2:
        while blue[r][c_idx] == 0 and blue[r][c_idx+1] == 0 and c_idx < 4: #c_idx 가 최대 3이여야 함 다음 줄을 실행하기 위해.
            c_idx += 1
        if blue[r][c_idx] == 1 or blue[r][c_idx+1] == 1:
            c_idx -= 1
        blue[r][c_idx+1] = 1
    elif t == 3:
        while blue[r][c_idx] == 0 and blue[r+1][c_idx] == 0 and c_idx < 5:
            c_idx += 1
        if blue[r][c_idx] == 1 or blue[r+1][c_idx] == 1:
            c_idx -= 1
        blue[r+1][c_idx] = 1

    blue[r][c_idx] = 1
    

def get_blue_score():
    cnt = 0
    for c in range(2, 6):
        for r in range(4):
            if blue[r][c] == 0:
                break
        else:
            cnt += 1
            for r in range(4):
                blue[r][c] = 0
            
            #column push 하기
            for temp_c in range(c, 0, -1): #c~1까지 돎
                for r in range(4):
                    blue[r][temp_c] = blue[r][temp_c-1]
                    blue[r][temp_c-1] = 0
    return cnt

def push_blue():
    global blue
    cur_c = -1
    for c in range(2):
        for r in range(4):
            if blue[r][c] == 1:
                cur_c = c
                break
        #이걸 하면 안되지 않나??????????? - 형태인 값이면 cur_c 가 2가 돼야 하기 때문
        #아 이렇게 해야 함. 왜냐 c 가 0 ~ 1까지 이기 때문. 먼저 0 방문함.
        if cur_c != -1:
            break
    #연한 곳에 숫자가 없을 경우
    if cur_c == -1:
        return
    
    temp_blue = [[0] * 6 for _ in range(4)]
    push_num = 0
    
    #2칸 밀기
    if cur_c == 0:
        push_num = 2
    #1칸 밀기
    if cur_c == 1:
        push_num = 1
    
    for c in range(2, 6):
        for r in range(4):
            temp_blue[r][c] = blue[r][c-push_num]
    
    blue = [temp[:] for temp in temp_blue]


def green_insert(t, y):
    r_idx = 0
    c = y
    if t == 1:
        while green[r_idx][c] == 0 and r_idx < 5:
            r_idx += 1
        if green[r_idx][c] == 1:
            r_idx -= 1

    elif t == 2:
        while green[r_idx][c] == 0 and green[r_idx][c+1] == 0 and r_idx < 5:
            r_idx += 1
        if green[r_idx][c] == 1 or green[r_idx][c+1] == 1:
            r_idx -= 1
        green[r_idx][c+1] = 1

    elif t == 3:
        while green[r_idx][c] == 0 and green[r_idx+1][c] == 0 and r_idx < 4:
            r_idx += 1
        if green[r_idx][c] == 1 or green[r_idx+1][c] == 1:
            r_idx -= 1
        green[r_idx+1][c] = 1
    
    green[r_idx][c] = 1

def get_green_score():
    cnt = 0
    #앞에서 부터 full stack 찾으면 full stack이 여러개 존재할 수도 있다는 것 고려하지 않아도됨
    for r in range(2, 6):
        for c in range(4):
            if green[r][c] == 0:
                break
        else:
            cnt += 1
            for c in range(4):
                green[r][c] = 0
            #delete
            for temp_r in range(r, 0, -1):
                for c in range(4):
                    green[temp_r][c] = green[temp_r-1][c]
                    green[temp_r-1][c] = 0
    return cnt

def push_green():
    global green
    cur_r = -1
    for r in range(2):
        for c in range(4):
            if green[r][c] == 1:
                cur_r = r
                break
        if cur_r != -1:
            break
    if cur_r == -1:
        return
    
    temp_green = [[0] * 4 for _ in range(6)]
    push_num = 0
    #2칸 밀기
    if cur_r == 0:
        push_num = 2
    #1칸 밀기
    elif cur_r == 1:
        push_num = 1
    
    for r in range(2, 6):
        for c in range(4):
            temp_green[r][c] = green[r-push_num][c]

    green = [temp[:] for temp in temp_green]



N = int(input())
blue = [[0] * 6 for _ in range(4)]
green = [[0] * 4 for _ in range(6)]
score = 0

for _ in range(N):
    t, x, y = map(int, input().split())

    #blue 넣기
    blue_insert(t, x)
    #blue 점수 계산하기 + push 해주기
    score += get_blue_score()
    #연한 칸 블록 있으면 밀기
    push_blue()


    #green 넣기
    green_insert(t, y)
    #green 점수 계산하기 + push 해주기
    score += get_green_score()
    #연한 칸 블록 있으면 밀기
    push_green()

block_cnt = 0

#파란색 타일 count
for r in range(4):
    for c in range(2, 6):
        if blue[r][c] == 1:
            block_cnt += 1

#초록색 타일 count
for r in range(2, 6):
    for c in range(4):
        if green[r][c] == 1:
            block_cnt += 1

print(score)
print(block_cnt)