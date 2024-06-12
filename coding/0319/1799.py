import sys
input = sys.stdin.readline

N = int(input())
map_ = []
for i in range(N):
    map_.append(list(map(int,input().split())))

#넣을 수 있는 1인 칸에 대해서 넣을지, 안넣을 지 다 해본다. 
#끝까지 다해보아야 함.

# dx = [-1, 1, 1, -1] #시계방향
# dy = [1, 1, -1, -1]
dx = [1,1]
dy = [1,-1]
placed_b = 0

def play_chess(map_, i,j, total):
    print(total)
    global placed_b
    #map_에 bishop 놓은 자리 + 대각선 위치에 1넣고 play_chess 재귀로 부르기
    if j>=N:
        i+= 1
        j = 0
    
    print(i,j)

    #map_[i][j]가 마지막 1일 경우 break문 작성하기
    if i == N-1 and j == N-1:
        return total
        #sys.exit()

    #가지치기 해줘야 하는 부분

    if map_[i][j] == 0:
        play_chess(map_,i,j+1, total)

    elif map_[i][j] == 1:
        #안넣을 떄
        map_[i][j] = 0
        #deep copy...
        play_chess(map_,i,j+1,total+1)

        #넣을 때
        #map_[i][j] = 1
        #대각선 쭉 끝까지 체크해줘야 함.
        for _ in range(1, N-i+1):
            for dir in range(2):
                nx = dx[dir]*_ + i
                ny = dy[dir]*_ + j

                #움직일 수 있는 대각선일 경우 0으로 바꿔줌
                if 0<=nx<N and 0<=ny<N and map_[nx][ny] == 1:
                    map_[i][j] = 0
        total += 1
        play_chess(map_,i,j+1,total+1)

    #placed_b 계속 max 값으로 update해주기

print(play_chess(map_, 0,0,0))