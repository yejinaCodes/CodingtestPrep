import sys

input = sys.stdin.readline

s1,s2,s3 = map(int,input().split())

result = {}
for i in range(1, s1+1):
    for j in range(1, s2+1):
        for k in range(1, s3+1):
            check = i+j+k
            if check in result:
                result[check] += 1
            else:
                result[check] = 1

print(max(result, key=result.get))

