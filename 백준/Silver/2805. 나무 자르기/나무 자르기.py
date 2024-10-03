import sys
input = sys.stdin.readline

N, M = map(int, input().split())
Tree = list(map(int, input().split()))

start = 0
end = max(Tree)
answer = 0
while start <= end:
    mid = (start + end) // 2
    total = 0
    for tree in Tree:
        if tree > mid:
            total += tree - mid
    if total >= M:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)