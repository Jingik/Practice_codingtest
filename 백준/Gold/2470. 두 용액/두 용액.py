import sys
input = sys.stdin.readline

N = int(input())
List = list(map(int, input().split()))

left, right = 0, N-1
Max_total = 0
min_sum = float('inf')
List.sort()
Result = []
while left < right:
    total = List[left] + List[right]
    if min_sum > abs(total):
        min_sum = abs(total)
        Result = [List[left], List[right]]
    if total > 0:
        right -= 1
    elif total < 0:
        left += 1
    else:
        break
        
print(*Result)
