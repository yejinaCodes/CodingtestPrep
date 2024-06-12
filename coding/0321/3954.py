import sys
input =sys.stdin.readline

T = int(input())
answer = []
for testcase in range(T):
    memory_size, program_code_size, input_size = map(int,input().split())

    memory = [0]*memory_size
    program_code = str(input())
    brackets = []
    for i in range(program_code_size):
        if program_code[i] == '[' or ']':
            brackets.append(i)

    input_array = str(input())

    #5*10^7이상일 경우 무한 루프임
    check_loop = 0
    start_pointer = 0
    
    program_pointer = 0
    red_flag = False

    loop_a = 0
    loop_b = 0

    #program pointer가 program의 마지막까지 올때까지 실행해야 하기 때문.
    while program_pointer < program_code_size:
        current = program_code[program_pointer]
        #brackets_pointer 사용해야 할 것 같음.

        if check_loop >= 50000000:
            red_flag = True
            break

        if current == '+':
            memory[start_pointer] += 1
            check_loop += 1
            program_pointer += 1


        elif current == '-':
            memory[start_pointer] -= 1
            check_loop += 1
            program_pointer += 1

        elif current == '>':
            start_pointer += 1
            if start_pointer == memory_size:
                start_pointer = 0
            check_loop += 1
            program_pointer += 1

        elif current == '<':
            start_pointer -= 1
            check_loop += 1
            program_pointer += 1

        elif current == '[':
            check_loop += 1
            loop_a = program_pointer
            if memory[start_pointer] == 0:
                #]다음으로 점프하기
                for x in range(len(brackets)):
                    if brackets[x] == program_pointer:
                        program_pointer = brackets[x+1]

        elif current == ']':
            check_loop += 1
            loop_b = program_pointer
            if memory[start_pointer] != 0:
                #[의 다음 명령으로 점프하기. 자신과 짝인 경우에 대해
                for x in range(len(brackets)):
                    if brackets[x] == program_pointer:
                        program_pointer = brackets[x-1]


        elif current == '.':
            check_loop += 1
            program_pointer += 1
            #출력 불필요
        elif current == ',':
            check_loop += 1
            program_pointer += 1
            #문자 저장 불필요
        
        #program_pointer += 1
    
    if red_flag:
        #루프 도는 구간을 알고 있어야 함.
        answer.append(('Loops', loop_a, loop_b))
    else:
        answer.append('Terminates')

for a in answer:
    print(a)