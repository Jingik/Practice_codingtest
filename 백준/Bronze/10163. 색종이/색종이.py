T = int(input())
board = [[0] * 1001 for _ in range(1001)]
def color(row,col,board,k):
    for i in range(x, x+row):
        for j in range(1000-y, 1000-y-col,-1):
            board[i][j] = k
    return board


for k in range(1, T+1):
    x, y, row, col = map(int, input().split())
    board = color(row,col,board,k)


for i in range(1, T+1):
    result = 0
    for box in board:
         result += box.count(i)
    print(result)