#Delete가 이루어질때 minheap, maxheap간에 싱크가 맞춰져야 하기 떄문에
#별도의 id 값을 사용해서 이미 삭제된 데이터인지를 확인한다.
#확인할 떄에는 deleted라는 리스트 안에 True, False 값이 들어가게 된다. 

import sys
import heapq

input = sys.stdin.readline
T = int(input())

def poppoop(heap):
    while len(heap)> 0:
        data, id = heapq.heappop(heap)
        if not deleted[id]: #처음 삭제하는 원소일 경우 deleted 체크해주기
            deleted[id] = True
            return data
    return None

for testcase in range(T):
    k = int(input())
    minheap = []
    maxheap = []
    count = 0
    deleted = [False]* (k+1)
    for i in range(k):
        operation, num = input().split()
        if operation == 'I':
            heapq.heappush(minheap, (int(num), count))
            #부호 바꿔서 push하기
            heapq.heappush(maxheap, (-int(num), count))
            count += 1

        ######
        elif operation == 'D':
            if int(num) == -1:
                poppoop(minheap)
                #heapq.heappop(minheap)
                #heapq.heappop(maxheap, -check)
                
            elif int(num) == 1:
               poppoop(maxheap)
                #부호 바꿔서 사용하기
               #-heapq.heappop(maxheap)
               #minheap.pop(check)

    
    max_value = poppoop(maxheap)
    if max_value == None:
        print('EMPTY'+ '/n')
    else:
        #max_value는 min_heap에서 delete됨
        heapq.heappush(minheap, (-max_value, count))
        print(-max_value, poppoop(minheap))


    # if len(minheap)== 0 or len(maxheap)==0:
    #     print('EMPTY')
    # else:
    #     maximum= (-heapq.heappop(maxheap))
    #     minimum= heapq.heappop(minheap)
    #     print(maximum, minimum, end=' ')