import sys

input = sys.stdin.readline

n = int(input())
cranes = list(map(int,input().split()))
m = int(input())
boxes = list(map(int,input().split()))

cranes.sort(reverse=True)
boxes.sort(reverse=True)

count = 0

if boxes[0] > cranes[0]:
    count = -1
else:
    while len(boxes)>0:
        for crane in cranes:
            #이 부분이 중요함...
            #지금 선택한 crane이 남아있는 박스 중 가장 가벼운 박스를 옮기지 못한다면 continue
            #그럼 끝까지 search 하지 않아도되기 때문
            if boxes and crane < boxes[-1]:
                continue

            for box in boxes:
                if box <= crane:
                    boxes.remove(box)
                    break
        count += 1

print(count)