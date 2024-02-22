import sys
from collections import deque
sys.setrecursionlimit(1000 ** 2)


def isvaild(x,y,N):
    if 0 <= x < N and 0 <= y < N:
        return True
    else:
        return False 

def Bfs(List,N):
    Queue = deque([List])
    count = 1
    Board[List[0]][List[1]] = 0
    while Queue:
        point = Queue.popleft()
        for dir in Direction:
            nx = point[0] + dir[0]
            ny = point[1] + dir[1]
            if isvaild(nx, ny, N):
                if Board[nx][ny] == 1:
                    Queue.append([nx,ny])
                    Board[nx][ny] = 0
                    count += 1
    return count
    
N = int(input())
Board = [list(map(int, input())) for _ in range(N)]
Direction = [(1, 0), (-1, 0), (0, 1), (0, -1)] # 아래, 위, 오른쪽, 왼쪽
count_house = []
for i in range(N):
    for j in range(N):
        if Board[i][j] == 1:
            count_house.append(Bfs([i,j],N))
print(len(count_house))
count_house.sort()
for ct in count_house:
    print(ct)