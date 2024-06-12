#stack 사용하기
#모든 오큰수에 대해 디폴트로 -1
#시각복잡도 때문에 stack으로 구현해야함
#stack에는 오큰수를 찾지 못한/찾는 중이 값들이 들어있음.
#stack을 사용하지 않으면 시간초가 뜸

n = int(input())
As = list(map(int, input().split()))

okunsu = [-1] * n

#tuple형식으로 값,인텍스를 넣어야 함.

stack = [] 
for _ in range(n):
    num = As[_]

    if len(stack) == 0 or stack[-1][0] >= num:
        stack.append((num, _))
    else:
        while len(stack) > 0:
            left_num, index = stack.pop()
            if left_num >= num:
                stack.append((left_num, index))
                break
            else:
                okunsu[index] = num
        stack.append((num, _))


for i in okunsu:
    print(i, end=' ')



            #if, else 순서 생각해서 짲기
    
            #break를 꼭 해줘야 함.
        #이전 값들에 대해서 오큰수를 search 한 뒤에 해당 값을 넣어줘야 함.
        #해당 값에 대해서도 오큰수를 구해야 하기 때문에 stack에 넣어준다