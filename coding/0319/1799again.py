import sys
import copy
input = sys.stdin.readline

results = []

def ExceptColor(arr,color):
    for i in range(N):
        for j in range(N):
            if color == "white":
                if (i+j)%2 == 0:
                    arr[i][j] = 0
            if color == "black":
                if (i+j)%2 != 0:
                    arr[i][j] = 0

def CheckCollision(x,y,bishops):
    for bishop in bishops:
        dx,dy = bishop[0], bishop[1]
        #slop가 같은 경우 대각선에 위치함
        if abs(dx-x) == abs(dy-y):
            return True
    return False


def Backtracking(x,y,board,bishops):
    #마지막 row(행)에서 마지막 column(렬)이후를 의미
    if y == N and x == N-1:
        global results
        results.append(len(bishops))
        return
    #다음 행으로 이동
    if y == N:
        Backtracking(x+1,0,board,bishops)
        return
    #bishop을 놓을 수 있다면
    if board[x][y] == 1 and not CheckCollision(x,y,bishops):
        #놓거나
        board[x][y] = 2
        bishops.append((x,y))
        Backtracking(x, y+1, board, bishops)
        board[x][y] = 1
        bishops.pop()
        #놓지 않거나
        Backtracking(x,y+1,board,bishops)
    else:
        Backtracking(x, y+1, board, bishops)


N = int(input())
board = [[0]*N for _ in range(N)]
white_board = None
black_board = None
for i in range(N):
    board[i]= list(map(int,input().split()))

white_board = copy.deepcopy(board)
black_board = copy.deepcopy(board)
#특정 색 제외시켜주기
ExceptColor(white_board, "black")
ExceptColor(black_board, "white")

bishops = []
white_count = 0
black_count = 0

Backtracking(0,0,white_board, bishops)
white_count = max(results)
results = []
Backtracking(0,0,black_board, bishops)
black_count = max(results)
print(white_count + black_count)

