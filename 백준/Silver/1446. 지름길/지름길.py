import sys
input = sys.stdin.readline

N, D = map(int, input().split())
shortcuts = []

for _ in range(N):
    start, end, length = map(int, input().split())
    if end <= D: 
        shortcuts.append((start, end, length))


dist = [i for i in range(D + 1)]

for i in range(D + 1):
    if i > 0:
        dist[i] = min(dist[i], dist[i - 1] + 1)  
    for start, end, length in shortcuts:
        if i == start and dist[i] + length < dist[end]:
            dist[end] = dist[i] + length  

print(dist[D])
