import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())
List = list(map(int, input().split()))

heapq.heapify(List)

for _ in range(m):
    x = heapq.heappop(List)
    y = heapq.heappop(List)
    new_card = x + y
    heapq.heappush(List, new_card)
    heapq.heappush(List, new_card)

print(sum(List))
