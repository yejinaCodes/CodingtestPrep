#길을 만들수 없는지 확인하는게 좋음 아니면 반대로 길을 만들 수 있는지 확인하는게 좋음?
#return False case를 만들지만 모든 if문을 통과할 경우 마지막에 return True.
#시간복잡도는 몇이 되는거임?
import sys
input = sys.stdin.readline

N, L = map(int,input().split())
map_ = [list(map(int,input().split())) for i in range(N)]

result = 0
def check_road(map):
    visited = [False for j in range(N)]
    for i in range(0, N-1):
        #두 숫자가 같을 경우
        if map[i] == map[i+1]:
            continue
        #두 숫자의 차이가 1이 넘을 경우
        elif abs(map[i]-map[i+1]) > 1:
            return False
        #두 숫자의 차이가 1일 경우 왼쪽 높이가 높을 경우:
        elif map[i] > map[i+1]:
            tmp = map[i+1]
            #L 거리만큼 이후 숫자들의 값이 같은지 확인
            for _ in range(i+1, i+L+1):
                if 0 <= _ < N:
                    #경사 높이가 같지 않을 경우
                    if map[_] != tmp:
                        return False
                    #이미 경사가 놓여진 경우
                    elif visited[_]:
                        return False
                    visited[_] = True
                #경사 범위가 범위를 벗어날 경우 경사를 놓을 수 없기 때문.
                else:
                    return False
        #오른쪽 숫자가 더 높을 경우
        #elif map[i] < map[i+1]:
        else:
            tmp = map[i]
            #print('chekc')
            #print(i)
            #이전값들을 확인하기
            for _ in range(i,i-L,-1):
                #print('chch')
                #print(_)
                if 0 <= _ < N:
                    if tmp != map[_]:
                        return False
                    elif visited[_]:
                        return False
                    visited[_] = True
                else:
                    return False
    #모든 경우를 다 돌고 return False를 하지 않았을 경우
    return True

#가로
for i in map_:
    if check_road(i):
        result += 1

#세로
for i in range(N):
    tmp = []
    for j in range(N):
        tmp.append(map_[j][i])
    if check_road(tmp):
        result += 1

print(result)