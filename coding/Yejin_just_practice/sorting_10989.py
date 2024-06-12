import sys
input = sys.stdin.readline

n = int(input())

llist = [0]*10001
for i in range(n):
    num = int(input())
    llist[num] += 1

#print('answer')
for i in range(len(llist)):
    if llist[i] == 0:
        continue
    else:
        for j in range(llist[i]):
            print(i)