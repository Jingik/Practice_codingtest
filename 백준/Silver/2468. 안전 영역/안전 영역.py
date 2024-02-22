import sys
from copy import deepcopy
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(100000)

direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def isvalid(x,y,N):
    if 0 <= x < N and 0 <= y < N:
        return True
    else:
        return False

def Bfs(List, N, number):
    Queue = deque([List])
    if Cp_board[List[0]][List[1]] > number:
        Cp_board[List[0]][List[1]] = number
    while Queue:
        point = Queue.popleft()
        for dir in direction:
            nx = point[0] + dir[0]
            ny = point[1] + dir[1]
            if isvalid(nx,ny,N):
                if Cp_board[nx][ny] > number:
                    Cp_board[nx][ny] = number
                    Queue.append([nx,ny])                    
        
N = int(input())
Board = []
maxNum = 0
for i in range(N):
    Board.append(list(map(int, input().split())))
    for j in range(N):
        if Board[i][j] > maxNum:
            maxNum = Board[i][j]
             
Max = 0
for x in range(maxNum):
    Cp_board = deepcopy(Board)
    Count = 0
    for i in range(N):
        for j in range(N):
            if Cp_board[i][j] > x:
                Count += 1   
                Bfs([i,j], N, x)
    if Max < Count:
        Max = Count
print(Max)