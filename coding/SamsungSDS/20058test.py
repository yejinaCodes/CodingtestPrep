test = [[0,3,2,9,3,1,6,7],
        [3,2,6,4,3,5,6,1],
        [5,6,7,8,8,4,5,6],
        [6,3,4,4,6,6,2,3],
        [4,5,5,2,3,6,5,1],
        [3,4,4,5,1,2,3,1],
        [4,5,2,6,5,7,8,9],
        [4,6,7,3,9,7,0,7]]

for i in range(0,8,2):
    for j in range(0,8,2):
        print(test[i][j])


new_board[x + i][y + r_size - j - 1] = board[x + j][y + i]