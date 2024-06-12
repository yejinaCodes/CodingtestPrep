import sys
input = sys.stdin.readline

def move(c):
    global data_pointer, memory_size, data_idx, input_size, code_idx, code_size, max_code_idx
    if c == "-":
        data_array[data_pointer] -= 1
        #왜 modulo 2^8을 해주는 거지?
        '''
        -1 divided by 10 equals 0 with a remainder of -1, 
        but since the modulus operator returns the positive remainder, it's 9.
        This behavior ensures that the modulus operation follows 
        a consistent mathematical convention
        '''
        data_array[data_pointer] %= 256
    elif c == "+":
        data_array[data_pointer] += 1
        data_array[data_pointer] %= 256
    elif c == "<":
        data_pointer -= 1
        data_pointer %= memory_size
    elif c == ">":
        data_pointer += 1
        data_pointer %= memory_size
    elif c == "[":
        if data_array[data_pointer] == 0:
            code_idx = brackets[code_idx]
    elif c == "]":
        if data_array[data_pointer] != 0:
            code_idx = brackets[code_idx]
    elif c == ".":
        pass
    elif c == ",": #이 부분 해줘야 함. -+ 존재하기 때문, 0인지 체크하기 떄문
        if data_idx < input_size:
            #ordinal position으로 unicode(10진수)로 값 변환. 문자의 순서 위치 값
            data_array[data_pointer] = ord(data[data_idx])
            data_idx += 1
        else:
            data_array[data_pointer] = 255

def loop_check():
    global code_idx, code_size, max_code_idx
    cnt = 0
    while code_idx < code_size:
        cnt += 1
        #하나의 프로그램 코드를 move 모듈에 보내기
        move(code[code_idx])
        #한번의 무한 루프에서 실행되는 명령어 개수가 50,000,000이기 때문에 [ 위치를 지정해주고 해당 위치에서 
        #해당 [] 위치에서 무한루프가 다시 발생할 경우 그 다음 if 문에 들어간다.
        if cnt >= 50000000:
            max_code_idx = min(max_code_idx, code_idx)
        code_idx += 1
        if cnt >= 2*50000000:
            print("Loops", max_code_idx, brackets[max_code_idx])
            return
    print("Terminates")
    return


# [] 위치 정보 미리 계산해놓기
def find_loop(code):
    brackets ={}
    tmp = []
    for idx, c in enumerate(code):
        if c == "[":
            tmp.append(idx)
        elif c == "]":
            from_ = tmp.pop()
            brackets[idx] = from_
            brackets[from_] = idx
    return brackets



T = int(input())
for testcase in range(T):
    memory_size, code_size, input_size = map(int,input().split())

    code = input().rstrip()
    data = input().rstrip()
    #초기 데이터 배열을 0으로 초기화
    data_array = [0] * memory_size
    data_pointer = 0
    code_idx = 0
    data_idx = 0
    # [] 위치 기록
    brackets = find_loop(code)
    max_code_idx = code_size
    loop_check()