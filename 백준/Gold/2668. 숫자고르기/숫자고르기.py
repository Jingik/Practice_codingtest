import sys
input = sys.stdin.readline

n = int(input())
graph = [0] + [int(input()) for _ in range(n)]
result = []

def dfs(node, resul):
    go = graph[node]
    visited[node] = True
    if not visited[go]:
        dfs(go, resul)
    elif visited[go] and go == resul:
        result.append(resul)

for i in range(1, n+1):
    visited = [False] * (n+1)
    dfs(i,i)

result.sort
print(len(result))
print(*result, sep='\n')