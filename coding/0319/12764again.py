import sys
import heapq

input = sys.stdin.readline

N = int(input())
user_time = [list(map(int,input().split())) for _ in range(N)]
user_time.sort()

#자리 count
used_cnt = [0]* N
used_cnt[0] = 1

#사용중인 컴퓨터 끝나는 시간과 자리 번호
occupied = []
heapq.heappush(occupied, [user_time[0][1], 0]) 
#자리 count와 seats_left가 index 0 부터 시작하기 때문. 첫번째 자리가 곧 0 index이기 때문.

#앞 자리를 뽑기위해 남아있는 자리들을 저장하는 리스트 사용하기
seats_left = [i for i in range(N)]
heapq.heapify(seats_left)
heapq.heappop(seats_left)

#두번째부터 시작
for user in user_time[1:]:
    start, end = user

    #제일 빨리 끝나는 uswer보다 시작시간이 늦으면 새로운 자리 차지
    if occupied[0][0] > start:
        new_posi = heapq.heappop(seats_left)
        used_cnt[new_posi] += 1
        heapq.heappush(occupied, [end, new_posi])
    else:
        #사용중인 자리가 여러군데 끝나있는 경우
        while True:
            prev_end, prev_seat = heapq.heappop(occupied)
            #그 다음 자리가 이미 끝나있는 경우 계속 seats_left에 넣어줘서 제일 작은 값을 찾기
            if occupied and occupied[0][0] <= start:
                heapq.heappush(seats_left, prev_seat)
                continue
            else:
                #해당 자리만 끝나있는 경우/더 이상 끝나있는 자리가 없을 경우
                new_posi = heapq.heappushpop(seats_left, prev_seat)
                heapq.heappush(occupied, [end, new_posi])
                used_cnt[new_posi] += 1
                break

#모두 컴터 사용후 자리 count 확인
idx = N - used_cnt.count(0)
print(idx)
print(' '.join(list(map(str,used_cnt[:idx]))))