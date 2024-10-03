import sys
from collections import deque

input = sys.stdin.readline

N, S = map(int, input().split())
List = list(map(int, input().split()))

# 부분 합 중 가장 짧은 길이
left, right = 0, 0
Max_total = 0
min_length = 1e9
while True:
    if Max_total >= S:
        min_length = min(min_length, right-left)
        Max_total -= List[left]
        left += 1
    elif right == N:
        break
    else:
        Max_total += List[right]
        right += 1

if min_length == 1e9:
    print(0)
else:
    print(min_length)