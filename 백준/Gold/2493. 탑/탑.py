import sys
input = sys.stdin.readline

N = int(input())
top = list(map(int, input().split()))
result = [0] * N
stack = []
for i in range(N):
    while stack and top[stack[-1]] <= top[i]:
        stack.pop()
    if stack:
        result[i] = stack[-1] + 1
    stack.append(i)

print(*result)

