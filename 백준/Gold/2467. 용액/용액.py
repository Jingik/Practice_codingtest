import sys
input = sys.stdin.readline

N = int(input())
total = float('inf')

right = N - 1
left = 0
List = list(map(int, input().split()))
List.sort()
total_stack = []
while left < right:
    current = List[right] + List[left]
    if abs(current) <= total:
        total = abs(current)
        total_stack = [List[left], List[right]]
        
    if current < total: 
        left += 1
    else:
        right -= 1

print(*total_stack)