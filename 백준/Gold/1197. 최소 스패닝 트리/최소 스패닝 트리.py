import sys
from queue import PriorityQueue 
input = sys.stdin.readline

V, E = map(int, input().split())

# Union Find 리스트
lst = [x for x in range(V + 1)]

# 가중치 기준 정렬을 위한 우선 순위 큐 
pq = PriorityQueue()

for i in range(E):
    u, v, w = map(int, input().split())
    pq.put((w, u, v)) # 튜플의 맨 앞의 값을 기준으로 정렬하므로, 가중치를 맨 앞에 위치시켜 put

def find(a):
    if a == lst[a]:
        return a
    lst[a] = find(lst[a])
    return lst[a]

def isSameSet(a, b):
    a = find(a)
    b = find(b)
    return a == b 

def union(a, b):
    a = find(a)
    b = find(b)
    lst[b] = a

edgeCnt = 0 # 간선 사용 횟수
result = 0 # 최소 신장 트리의 가중치

while edgeCnt < (V - 1): 
    w, u, v = pq.get()
    if not isSameSet(u, v):
        union(u, v)
        edgeCnt += 1
        result += w

print(result)