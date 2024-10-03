import sys
from collections import deque

input = sys.stdin.readline

def bfs():
    # BFS 큐
    queue = deque([1])
    visited[1] = True
    cnt = 0
    while queue:
        for _ in range(len(queue)):
            x = queue.popleft()
            if x == 100:
                return cnt
            for i in range(1, 7):
                next_pos = x + i
                if next_pos <= 100:
                    if next_pos in ladder_snake:
                        next_pos = ladder_snake[next_pos]
                    if not visited[next_pos]:
                        visited[next_pos] = True
                        queue.append(next_pos)
        cnt += 1
                    
    return -1 

# 사다리와 뱀 정보 입력
N, M = map(int, input().split())
ladder_snake = {}

for _ in range(N + M):
    x, y = map(int, input().split())
    ladder_snake[x] = y

visited = [False] * 101 
visited[0] = True
print(bfs())
