import sys

def input():
    return sys.stdin.readline()


def input_data():
    H, W = map(int, input().split())
    blocks = list(map(int, input().split()))

    grid = [[1] * W for _ in range(H)]

    for col in range(W):
        none_block = H - blocks[col]
        for row in range(none_block):
            grid[row][col] = 0

    return H, W, grid


def solution():
    H, W, grid = input_data()
    rain = 0

    for row in range(H):
        temp = grid[row]

        t = []
        for col in range(W):
            if temp[col] == 1:
                t.append(col)

        if len(t) <= 1: continue

        for idx in range(len(t)-1):
            rain += t[idx+1] - t[idx] - 1

    return rain

print(solution())