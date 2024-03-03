import sys
input = sys.stdin.readline 

def New_board(x, y, target, board):
    i = 1
    ny = y
    nx = 0
    while i < x * y:
        for dir in direction:
            nx += dir[1]
            ny += dir[0]
            while 0 <= nx < x and 0 <= ny < y and board[ny][nx] == 0:
                board[ny][nx] = i
                i += 1
                if board[ny][nx] == target:    
                    return print(nx + 1, y - ny)
                nx += dir[1]
                ny += dir[0]
            nx -= dir[1]
            ny -= dir[0]
    return print(0)

direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
x, y = map(int, input().split())
target = int(input())
board = [[0] * x for _ in range(y)]
New_board(x, y, target, board)
