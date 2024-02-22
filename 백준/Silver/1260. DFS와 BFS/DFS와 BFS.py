import sys
from collections import deque

input = sys.stdin.readline

def Dfs(idx):
    Dfs_visited[idx] = 1
    Tree[idx].sort()
    print(idx, end = " ")
    for node in Tree[idx]:
        if Dfs_visited[node] == 0:
            Dfs(node)


            
def Bfs(idx):
    Queue = deque()
    Queue.append(idx)
    
    while Queue:
        X = Queue.popleft()
        Bfs_visited[X] = 1
        Tree[X].sort()
        for node in Tree[X]:
            if Bfs_visited[node] == 0:
                Queue.append(node)
                Bfs_visited[node] = 1
                print(node, end = " ")

N, M, V = map(int, input().split())
Tree = {i : [] for i in range(N + 1 )}
Dfs_visited = [0] * (N + 1)
Bfs_visited = [0] * (N + 1)
for _ in range(M):
    A, B = map(int, input().split())
    Tree[A] += [B]
    Tree[B] += [A]
Dfs(V)
print()
print(V, end = " ")
Bfs(V)
