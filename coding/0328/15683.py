import sys
input = sys.stdin.readline

N,M = map(int,input().split())
room = [list(map(int,input().split())) for _ in range(N)]

cctv = {1:[],2:[],3:[],4:[],5:[]}
just_cctvs = []
total_cctv = 0
wall = 0 

#초기화 세팅
for i in range(N):
    for j in range(M):
        if room[i][j] == 1:
            cctv[1].append((i,j))
            total_cctv +=1 
            just_cctvs.append((i,j))
        elif room[i][j] == 2:
            cctv[2].append((i,j))
            total_cctv +=1 
            just_cctvs.append((i,j))
        elif room[i][j] == 3:
            cctv[3].append((i,j))
            total_cctv +=1 
            just_cctvs.append((i,j))
        elif room[i][j] == 4:
            cctv[4].append((i,j))
            total_cctv +=1 
            just_cctvs.append((i,j))
        elif room[i][j] == 5:
            cctv[5].append((i,j))
            total_cctv +=1 
            just_cctvs.append((i,j))
        elif room[i][j] == 6:
            wall += 1
        else:
            continue


def check_horizontal(map_, i,j, type, watched):
    #type에 맞게 한 방향으로 쭉 값 바꿔주기
    #watched도 계산해주기
    if map_[i][j] == 1:
        if type == 0:

        elif type == 1:

        elif type == 2:

        elif type == 3:

    elif map_[i][j] == 2:
        if type == 0:
        
        elif type == 1:
    
    elif map_[i][j] == 3:
        if type == 0:
        
        elif type == 1:
        
        elif type == 2:
        
        elif type == 3:

    elif map_[i][j] == 4:
        if type == 0:
        
        elif type == 1:
        
        elif type == 2:
        
        elif type == 3:

    elif map_[i][j] == 5:
        for x in range(4):


    return watched


# range() 모든 경우의 수에 대해서 map_을 만들고 0을 계산해야 함. 

#for 안에 for 안에 for 안에 for 을 어떻게 표현하지?

#backtracking으로 풀어야 함!!

def backtracking(map_, i,j, blindspot):
    #어떤 기준으로 탈출할것인지.
    if map_[i][j] == 1:
        for x in range(4):
            check_horizontal(map_, i,j, x, blindspot)
            if len(just_cctvs) > 0:
                nextx, nexty = just_cctvs.pop()
                backtracking(map_,nextx,nexty, blindspot)
            else:
                return
    elif map_[i][j] == 2:
        for x in range(2):
            check_horizontal(map_, i,j, x, blindspot)
            if len(just_cctvs) > 0:
                nextx, nexty = just_cctvs.pop()
                backtracking(map_,nextx,nexty, blindspot )
            else:
                return
    elif map_[i][j] == 3:
        for x in range(4):
            check_horizontal(map_, i,j, x, blindspot)
            if len(just_cctvs) > 0:
                nextx, nexty = just_cctvs.pop()
                backtracking(map_,nextx,nexty, blindspot )
            else:
                return
    elif map_[i][j] == 4:
        for x in range(4):
            check_horizontal(map_, i,j, x, blindspot)
            if len(just_cctvs) > 0:
                nextx, nexty = just_cctvs.pop()
                backtracking(map_,nextx,nexty, blindspot)
            else:
                return
    elif map_[i][j] == 5:
        check_horizontal(map_,i,j,x, blindspot)
        if len(just_cctvs) > 0:
                nextx, nexty = just_cctvs.pop()
                backtracking(map_,nextx,nexty, )
        else:
            return



blindspot = (N*M) - total_cctv - wall
firstx, firsty = just_cctvs.pop()
backtracking(room, firstx, firsty, blindspot)

#blindspot도 계산해주어야 함....!!!!
