import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, adj):
    rtn = 0
    q = deque()
    q.append(x)
    visited[x] = True

    while q:
        v = q.popleft()
        for n in adj[v]:
            if not visited[n]:
                q.append(n)
                visited[n] = True
                rtn += 1
    return rtn


N, M, X = map(int, input().split())

higher = [[] for _ in range(N+1)]
lower = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    A, B = map(int, input().split())
    higher[A].append(B)  # A보다 큰 학생들
    lower[B].append(A)   # B보다 작은 학생들

visited = [False] * (N+1)
print(1 + bfs(X, lower), end=" ")
visited = [False] * (N+1)
print(N - bfs(X, higher))
