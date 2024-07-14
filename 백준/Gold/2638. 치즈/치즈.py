import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
Map = []
total = 0

for i in range(n):
    Map.append(list(map(int, input().rstrip().split())))
    total += sum(Map[i])

direction = [(1,0), (0,1),(-1,0),(0,-1)]
time = 0

def isvalid(nx, ny, n, m):
    return 0 <= nx < n and 0 <= ny < m

def BFS():
    global n, m
    q = deque([(0,0)])
    visited[0][0] = 1

    while q:
        x, y = q.popleft()
        for dir in direction:
            nx = x + dir[0]
            ny = y + dir[1]
            if isvalid(nx, ny, n, m):
                if Map[nx][ny] == 0 and visited[nx][ny] == 0:
                    q.append([nx, ny])
                    visited[nx][ny] = 1
                elif Map[nx][ny] == 1:
                    visited[nx][ny] += 1

while True:
    visited = [[0 for _ in range(m)] for _ in range(n)]
    BFS()
    time += 1
    
    for i in range(n):
        for j in range(m):
            if visited[i][j] >= 2:
                Map[i][j] = 0

    Total = 0
    for i in range(n):
        for j in range(m):
            if Map[i][j] == 0:
                Total += 1
    
    if Total == (n * m):
        break

print(time)
