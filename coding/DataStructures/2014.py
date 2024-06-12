#minheap사용하면 됨. 
import sys
import heapq
input = sys.stdin.readline

k,n = map(int,input().split())
nums = list(map(int,input().split()))

#방문 처리는 왜 해줘야 하는거지?
#왜냐면 곱한 값이 똑같은게 또 나올 수도 있기 때문...

#그리고 최댓값보다 곱한 결과가 큰것을 왜 확인해줘야 하는거지?
#넣어져도 꺼내질 일이 없기 떄문에 넣지 않는다..
#heap가 n 길이보다 길어도 들어오는 값이 visited하지 않은 작은 값이라면 넣어줘야 함.
#어차피 n-1번 for loop을 돌기 때문에 pop은 원하는만큼 일어난다.

#n 번째에서의 최솟값을 출력하면 됨.

heap = []
for num in nums:
    heapq.heappush(heap, num)

#visited는 set으로 효율적으로 만들어주는게 좋음.
visited = set()
max_value = max(nums)

#마지막 k번째를 heap에서 뽑을 때는 for문을 다 나와서 출력하기.
for i in range(n-1):
    x = heapq.heappop(heap)

    for i in nums:
        current = x * i
        #아래 경우일 경우, 완벽히 heap뒷 부분에 들어갈 것이기 때문에 pop을 할 경우가 아예 없음.
        if len(heap) >= n and current > max_value:

            continue
        #곱한 값이 똑같은게 또 나올 수도 있기 때문에 체크해줘야 함.
        if current not in visited:
            heapq.heappush(heap, current)
            #set에는 add로 append해주는 거임.
            visited.add(current)
            max_value = max(max_value, current)

print(heapq.heappop(heap))