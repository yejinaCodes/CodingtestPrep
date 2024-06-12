#모든 경우의 수를 해보는 방법. dfs사용하기
def solution(coin, cards):
    from collections import deque
    import heapq
    cards = deque(cards)
    print(cards)
    def dfs(mycards, coin):
        #카드를 뽑을 수 있는지 aka 다음 라운드 진출 가능여부 파악
        x = cards.popleft()
        y = cards.popleft()
        #카드를 소유할 수 있는지
        if coin == 0:
            dfs(mycards, coin)
        #1개 카드만 소유
        elif coin == 1:
            dfs(mycards, coin)
            dfs(mycards, coin)
        #2개까지 소유 가능할때
        elif coin > 1:
            #2ro개 다 소유 
            dfs(mycards, coin)
            #1개만 소유
            
            #소유하지 않음
    
        pass
    
    answer = [] #max heap으로 사용
    #answer = 0
    return answer