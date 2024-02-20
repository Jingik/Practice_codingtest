def Dfs(idx):
    visited.append(idx)
    for node in Graph[idx]:
        if node not in visited:
            Dfs(node)

import sys
input = sys.stdin.readline
Node = int(input())
N = int(input())
visited = []
Graph = {i : [] for i in range(Node+1)}
for _ in range(N):
    a, b = map(int, input().split())
    Graph[a] += [b]
    Graph[b] += [a]
    
Dfs(1)

print(len(visited) - 1)