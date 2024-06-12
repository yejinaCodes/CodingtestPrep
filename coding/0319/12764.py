import sys
import heapq
input = sys.stdin.readline

N = int(input())
user_time = [(0,0)]
answer = []

for i in range(N):
    start,end = map(int,input().split())
    user_time.append((start,end))
user_time.sort()
seats = [0]*(N+1)
#print(user_time)

total_computer = 0

for i in range(1, N+1):
    if len(answer) == 0:
        heapq.heappush(answer,(user_time[i][1],i))
        seats[i] += 1
        #print(answer)
    else:
        if user_time[i][0] < answer[0][0]:
            heapq.heappush(answer,(user_time[i][1], i))
            #print(answer)
            seats[i] += 1
            #print(seats)
        else:
            #여기서 값이 여러개 가능할떄를 고려해줘야함. 작은 index를 골라줘야 하기 때문에 
            #다시 여기서 heapq를 사용한다.
            tmp = []
            #여기서 시간초과 뜨는 것 같음..
            while answer[0][0] <= user_time[i][0]:
                end,index = heapq.heappop(answer)
                heapq.heappush(tmp, (index, end))

            chosenindex, chosennum = heapq.heappop(tmp)
            for i in range(len(tmp)):
                heapq.heappush(answer, (tmp[i][1], tmp[i][0]))
            heapq.heappush(answer, (user_time[i][1], chosenindex))
            seats[chosenindex] += 1
            # end, index = heapq.heappop(answer)
            # #print(end, index)
            # heapq.heappush(answer, (user_time[i][1], index))
            # seats[index] += 1
            # #print(seats)

for value in seats:
    if value == 0:
        seats.remove(value)

print(len(seats))
print(*seats)