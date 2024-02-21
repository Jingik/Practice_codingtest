import sys;input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def Dfs(idx):
    for node in Tree[idx]:
        if visited[node] == 0:
            visited[node] = idx
            Dfs(node)

N = int(input())
Tree = {i : [] for i in range(N+1)}
visited = [0] * (N + 1)
for _ in range(N-1):
    A, B = map(int, input().split())
    Tree[A] += [B]
    Tree[B] += [A]

Dfs(1)
visited.pop(0)
visited.pop(0)
for x in visited:
    print(x)