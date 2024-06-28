import sys
sys.setrecursionlimit(10**6)
inpurt = sys.stdin.readline

def isvalid(x, y, M, N):
    return 0 <= x < M and 0 <= y < N

def dfs(x, y):
    if x == M - 1 and y == N - 1:
        return 1
    if DP[x][y] != -1:
        return DP[x][y]

    ways = 0
    for dir in Direction:
        dx, dy = x + dir[0], y + dir[1]
        if isvalid(dx, dy, M, N) and Map[x][y] > Map[dx][dy]:
            ways += dfs(dx, dy)
    
    DP[x][y] = ways
    return DP[x][y]

Direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
M, N = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(M)]
DP = [[-1] * N for _ in range(M)]

result = dfs(0, 0)
print(result)
