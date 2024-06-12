import sys
input = sys.stdin.readline

N = int(input())
blocks = []
for _ in range(N):
    blocks.append(list(map(int, input().split())))

green_matrix = [[0] * 4 for _ in range(6)]
blue_matrix = [[0] * 6 for _ in range(4)]
total_points = 0

def stack(type, x, y):
    #1x1
    if type == 1:
        for i in range(5, -1, -1):
            if green_matrix[i][y] == 0:
                green_matrix[i][y] = 1
                break
        for i in range(5, -1, -1):
            if blue_matrix[x][i] == 0:
                blue_matrix[x][i] = 1
                break
    #1x2
    elif type == 2:
        #사이에 낄 수도 있음!!
        for i in range(5, -1, -1):
            count = 0
            for ii in range(4):
                if green_matrix[i][ii] == 0:
                    count += 1
            if count == 4:
                green_matrix[i][y] = 1
                green_matrix[i][y+1] = 1
                break

        for i in range(4, -1, -1):
            if blue_matrix[x][i] == 0 and blue_matrix[x][i+1]:
                if sum(blue_matrix[x][:i-1]) == 0 or i == 0:
                    blue_matrix[x][i] = 1
                    blue_matrix[x][i+1] = 1
                    print(blue_matrix)
                    break
                break

        # for i in range(4, -1, -1):
        #     if blue_matrix[x][i] == 0 and blue_matrix[x][i+1] == 0:
        #         blue_matrix[x][i] = 1
        #         blue_matrix[x][i+1] = 1
        #         break
    #2x1
    elif type == 3:
        for i in range(4, -1, -1):
            if green_matrix[i+1][y] == 0 and green_matrix[i][y] == 0:
                green_matrix[i+1][y] = 1
                green_matrix[i][y] = 1
                break
        
        # for i in range(5, -1, -1):
        #     if blue_matrix[x][i] == 0 and blue_matrix[x+1][i] == 0:
        #         blue_matrix[x][i] = 1
        #         blue_matrix[x+1][i] = 1
        #         break
        #사이에 낄 수 있기 때문에!!
        for j in range(5, -1, -1):
            count = 0
            for ii in range(4):
                if blue_matrix[ii][j] == 0:
                    count += 1
            if count == 4:
                blue_matrix[x][j] = 1
                blue_matrix[x+1][j] = 1
                break

def shift(line, which):
    #한 칸씩 옮기기
    if which == 'green':
        for i in range(line-1, -1, -1):
            green_matrix[i+1] = green_matrix[i]
    
    elif which == 'blue':
        for j in range(line-1, -1, -1):
            for i in range(4):
                if blue_matrix[i][j] == 1:
                    blue_matrix[i][j+1] = 1
                    blue_matrix[i][j] = 0

#연한 곳은 체크할 필요 없음으로 일단 처리
#full 인 곳을 delete해주기
def check_full():
    global total_points
    #green
    for i in range(2, 6):
        if sum(green_matrix[i]) == 4:
            for j in range(4):
                green_matrix[i][j] = 0
            shift(i, 'green')
            total_points += 1
    #blue
    for i in range(2, 6):
        count = 0
        for j in range(4):
            if blue_matrix[j][i] == 1:
                count += 1
        if count == 4:
            for j in range(4):
                blue_matrix[j][i] = 0
            total_points += 1
            shift(i, 'blue')
            #print('check')


#이 부분 틀렸음.. 한번에 2개의 연한 box에 block이 있을수도 있음.
def check_vivid():
    #green
    for j in range(1, -1, -1):
        if sum(green_matrix[j]) > 0:
            for i in range(4):
                green_matrix[5][i] = 0
            shift(5, 'green')
            break

    #blue
    for j in range(1, -1, -1):
        count = 0
        for i in range(4):
            if blue_matrix[i][j] == 1:
                count += 1
                break
        if count != 0:
            for ii in range(4):
                blue_matrix[ii][5] = 0
            #print(blue_matrix)
            shift(5, 'blue')
            break

for _ in range(N):
    #1개의 블록에 대해서
    type, x, y = blocks[_]
    stack(type, x, y)
    check_full()
    # full 한 라인 다 delete 한 다음에 shift하는 건지
    # 한 번 delete 할때마다 shift하는 건지 헷갈렷음.
    check_vivid()

entire = 0

for i in range(4):
    entire += sum(blue_matrix[i])
for i in range(6):
    entire += sum(green_matrix[i])

print(total_points)
print(entire)

print(blue_matrix)
print()
print(green_matrix)
#연한곳은 전체 행, 렬 확인할 필요 없나?
