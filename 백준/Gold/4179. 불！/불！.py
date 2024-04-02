from collections import deque

di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]

def bfs(q):
    while q:
        x, y, s = q.popleft()

        for i in range(4):
            ni = x + di[i]
            nj = y + dj[i]

            if 0 <= ni < n and 0 <= nj < m:
                if not v[ni][nj] and arr[ni][nj] == '.':  
                    q.append((ni, nj, s))  
                    v[ni][nj] = v[x][y] + 1  
            else:
                if s == 'J':  
                    return v[x][y]  

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)] 
v = [[0]*m for _ in range(n)]

q = deque()

for i in range(n):
    for j in range(m):
        if arr[i][j] == 'J':  
            v[i][j] = 1
            q.append((i, j, 'J'))
        if arr[i][j] == 'F':  
            v[i][j] = 1
            q.appendleft((i, j, 'F'))

ans = bfs(q)

if ans:
    print(ans)
else:
    print('IMPOSSIBLE')