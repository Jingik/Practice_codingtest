import sys
import heapq
.
input = sys.stdin.readline

N = int(input())  
classes = [list(map(int, input().split())) for _ in range(N)]

classes.sort(key=lambda x: x[0])

heap = []

heapq.heappush(heap, classes[0][1])

for i in range(1, N):
    if heap[0] <= classes[i][0]:
        heapq.heappop(heap)

    heapq.heappush(heap, classes[i][1])

print(len(heap))
