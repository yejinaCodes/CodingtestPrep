import sys
input = sys.stdin.readline

n = int(input())

schedule = []
for i in range(n):
    schedule.append(list(map(int,input().split())))

#schedule입력 순서대로 다중정렬하기
schedule = sorted(schedule, key=lambda x: (x[0], -x[1]))
#시작일이 같을 경우 더 긴 스케줄을 우선으로 적기

#matrix 만들기
end = schedule[n-1][1]
matrix = []
for i in range(n):
    matrix.append([0]* (end+1))

#schedule입력하기
#겹치는 요일이 있는지 없는지 확인
#start,end,column 업데이트

result = 0
beginning = schedule[0][0] #인가?
ending = 0
column_highest = n

same = True
column = 0

while schedule:
    summation = 0
    start, end = schedule.pop(0)
    #column을 하나씩 다 확인
    for i in range(column_highest):
        if matrix[i][start] == 0:
            for j in range(start,end+1):
                matrix[i][j] = 1
            column = i
            break
    for i in range(n):
        summation += matrix[i][start]
    
    #같은 그룹인지 확인하기!!!!
    if summation > 1:
        calc = (end - beginning+1)*(column+1)
        result = calc
        print(result)
    else:
        calc = (end-start+1)*(column+1)
        result += calc

#print(result)



