import sys
input = sys.stdin.readline

N, M = map(int, input().split())
city = []
for i in range(N):
    city.append(list(map(int, input().split())))

homes = []
chicken_place = []
city_chicken = 1e9

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            homes.append((i,j))
        elif city[i][j] == 2:
            chicken_place.append((i,j))


#chicken_distance = [1e9 for _ in range(len(homes))]
check = [False for _ in range(len(chicken_place))]

def backtracking(idx, count):
    global city_chicken, check, chicken_place
    if count == M:
        tmp = 0
        #city_chicken 계산하기
        for home in homes:
            distance = 1e9
            for i in range(len(chicken_place)):
                #어떤 chicken을 선태했는지 check 에 True로 표현되어 있음.
                if check[i]:
                    calculate = abs(home[0] - chicken_place[i][0]) + abs(home[1] - chicken_place[i][1])
                    #각 집의 최소 치킨거리 update해주기
                    distance = min(distance, calculate)
            
            tmp += distance
        city_chicken = min(city_chicken, tmp)

        return
    
    for i in range(idx, len(chicken_place)):
        if not check[i]:
            check[i] = True
            backtracking(i+1, count+1)
            check[i] = False
    return

backtracking(0, 0)
        
print(city_chicken)