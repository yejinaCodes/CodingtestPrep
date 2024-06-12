import sys
import heapq
input = sys.stdin.readline

def median(heap):
    len_heap = len(heap)
    #heapq.heapify(heap)
    return (heap[len_heap//2])

T = int(input())
for testcase in range(T):
    num = int(input())

    num_list = list(map(int, input().split()))

    #input이 10개를 넘는 값에 대해서 += 해줘야 함.
    for i in range(num//10):
        num_list += list(map(int,input().split()))

    left_heap = [] #최대힙. median보다 작은 수
    right_heap = [] #최소힙. median보다 큰 수
    med_ian = num_list[0]
    result = [med_ian]
    for i in range(1, num):
        if num_list[i] <= med_ian:
            heapq.heappush(left_heap, -num_list[i])
        else:
            heapq.heappush(right_heap, num_list[i])
        #이게 결국 홀수부터임. 왜냐하면 첫번째는 이미 넣어놨기 때문. 두번째 값부터 시작함..
        if i%2 == 0:
            if len(left_heap) > len(right_heap):
                heapq.heappush(right_heap, med_ian)
                med_ian = -heapq.heappop(left_heap)
            elif len(left_heap) < len(right_heap):
                heapq.heappush(left_heap, -med_ian)
                med_ian = heapq.heappop(right_heap)
            result.append(med_ian)
    
    print(len(result))
    for i in range(len(result)):
        print(result[i], end=' ')
        #10번째 출력후 한 줄 띄우기
        if (i+1)%10 == 0:
            print()
    print()
        # heapq.heappush(heap, num_list[i])
        # #heapq.heapify(heap)
        # if (i+1)%2 !=0:
        #     #정렬을 수행하기
        #     heapq.heapify(heap)
        #     print(heap)
        #     result.append(median(heap))


#len(heap)//2 로 중간값 접근하기
    