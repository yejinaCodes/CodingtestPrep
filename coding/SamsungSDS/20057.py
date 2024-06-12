import sys
input = sys.stdin.readline

N = int(input())
maze = []
for i in range(N):
    maze.append(map(int, input().split()))

centerx, centery = N//2, N//2

dx = [0, -1, 0, 1] #좌하우상
dy = [-1, 0, 1, 0]


def sand_spread():
    #부는 방향에 따라 맞게 sand 비율 spread하기
    pass

#토네이도 회전 방향
times = 1
for _ in range(N): #총 도는 횟수 결국 N*2번이 됨.
    
    #for i in range(1, N):
    for i in range(2):
        x = (x+1)%4
        y = (y+1)%4
            #nx = dx[x] + centerx
            #ny = dy[y] + centery
    times += 1

